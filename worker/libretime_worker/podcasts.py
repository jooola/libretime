from cgi import parse_header
from pathlib import Path
from tempfile import NamedTemporaryFile
from typing import Any, Dict, Optional
from urllib.parse import urlsplit

import mutagen
import requests
from celery.utils.log import get_task_logger
from requests import RequestException, Response

logger = get_task_logger(__name__)


def ingest_podcast(
    item_id: int,
    url: str,
    callback_url: str,
    callback_api_key: str,
    podcast_name: str,
    override_meta: bool,
    track_title: Optional[str],
) -> Dict[str, Any]:
    result: Dict[str, Any] = {"episodeid": item_id}

    with NamedTemporaryFile(delete=False) as tmp_file:
        try:
            with requests.get(url, stream=True) as resp:
                resp.raise_for_status()

                filename = extract_filename(resp)
                for chunk in resp.iter_content(chunk_size=2048):
                    tmp_file.write(chunk)

        except RequestException as exception:
            result["status"] = 0
            result["error"] = str(exception)
            logger.error(f"could not download file: {exception}")
            return result

        # Save metadata
        metadata = mutagen.File(tmp_file.name, easy=True)
        if metadata is None:
            logger.warning(f"could not open {tmp_file.name} using mutagen!")

        if override_meta:
            logger.debug(f"overriding album name with podcast name {podcast_name}")
            metadata["artist"] = podcast_name
            metadata["album"] = podcast_name
            metadata["title"] = track_title

        elif "album" not in metadata:
            logger.debug(f"setting album name to podcast name {podcast_name}")
            metadata["album"] = podcast_name

        metadata.save()
        logger.info(f"saved metadata {metadata.pprint()}")

        # Upload file
        try:
            with requests.post(
                callback_url,
                files={"file": (filename, tmp_file)},
                auth=(callback_api_key, ""),
            ) as upload_resp:
                upload_resp.raise_for_status()
                upload_payload = upload_resp.json()

                result["fileid"] = upload_payload["id"]
                result["status"] = 1

        except RequestException as exception:
            result["status"] = 0
            result["error"] = str(exception)
            logger.error(f"could not upload file: {exception}")

    return result


def extract_filename(response: Response) -> str:
    if "Content-Disposition" in response.headers:
        _, params = parse_header(response.headers["Content-Disposition"])
        if "filename" in params:
            return params["filename"]

    return Path(urlsplit(response.url).path).name
