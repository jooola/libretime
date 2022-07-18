import sys
from enum import Enum
from pathlib import Path
from typing import List

import backoff
from api_clients.version1 import AirtimeApiClient as ApiClient
from jinja2 import Template
from loguru import logger
from pydantic import BaseModel, ValidationError, conlist
from requests.exceptions import ConnectionError, Timeout


class SourceOutputEnum(Enum):
    ICECAST = "icecast"


class SourceAudioTypeEnum(Enum):
    OGG = "ogg"
    MP3 = "mp3"


class SourceAudioChannelsEnum(Enum):
    STEREO = "stereo"
    MONO = "mono"


class Source(BaseModel):
    enabled: bool = False
    status: str = "OK"  # TODO: Use enum ?
    output: SourceOutputEnum = SourceOutputEnum.ICECAST

    # Meta
    name: str
    description: str
    url: str
    genre: str

    # Audio
    audio_type: SourceAudioTypeEnum = SourceAudioTypeEnum.OGG
    audio_channels: SourceAudioChannelsEnum = SourceAudioChannelsEnum.STEREO
    audio_bitrate: int = 256

    is_mobile: bool

    # Icecast
    icecast_host: str = "localhost"
    icecast_port: str = "8000"
    icecast_mount: str

    # Icecast Auth
    icecast_user: str
    icecast_password: str
    icecast_admin_user: str
    icecast_admin_password: str


class Config(BaseModel):
    sources: conlist(Source, min_items=1, max_items=4)

    master_live_stream_port: int = 8001
    master_live_stream_mount: str = "/master"
    show_live_stream_port: int = 8002
    show_live_stream_mount: str = "/show"

    # Icecast
    icecast_vorbis_metadata: bool = False

    # Meta
    off_air_meta: str = "Offline"
    output_sound_device: bool = False
    output_sound_device_type: str = "ALSA"  # TODO: Use enum ?
    log_filepath: str = "liquidsoap.log"
    auth_command: str = "libretime-liquidsoap auth"


here = Path(__file__).parent
config_template_path = here / "templates/config.liq.j2"
config_template = Template(config_template_path.read_text())


def generate_config(data: dict) -> str:
    try:
        data = Config(**data)
    except ValidationError as error:
        logger.critical(error)
        sys.exit(1)

    return config_template.render(**data)


def compat_generate_config(data: dict) -> dict:
    """
    Compatibility layer between received data and template data.

    This should be removed once we transmit data in the same form of
    the template data.
    """
    return {
        "sources": [
            map(
                lambda i: {
                    "enabled": data[f"{i}_enable"],
                    "status": data[f"{i}_liquidsoap_error"],
                    "output": data[f"{i}_output"],
                    "name": data[f"{i}_name"],
                    "description": data[f"{i}_description"],
                    "url": data[f"{i}_url"],
                    "genre": data[f"{i}_genre"],
                    # Audio
                    "audio_type": data[f"{i}_type"],
                    "audio_channels": data[f"{i}_channels"],
                    "audio_bitrate": data[f"{i}_bitrate"],
                    "is_mobile": data[f"{i}_mobile"],
                    # Icecast
                    "icecast_host": data[f"{i}_host"],
                    "icecast_port": data[f"{i}_port"],
                    "icecast_mount": data[f"{i}_mount"],
                    "icecast_user": data[f"{i}_user"],
                    "icecast_password": data[f"{i}_pass"],
                    "icecast_admin_user": data[f"{i}_admin_user"],
                    "icecast_admin_password": data[f"{i}_admin_pass"],
                },
                [1, 2, 3, 4],
            )
        ],
        "master_live_stream_port": data["master_live_stream_port"],
        "master_live_stream_mount": data["master_live_stream_mp"],
        "show_live_stream_port": data["dj_live_stream_port"],
        "show_live_stream_mount": data["dj_live_stream_mp"],
        # Icecast
        "icecast_vorbis_metadata": data["icecast_vorbis_metadata"],
        # Meta
        "off_air_meta": data["off_air_meta"],
        "output_sound_device": data["output_sound_device"],
        "output_sound_device_type": data["output_sound_device_type"],
        "log_filepath": "/var/log/airtime/pypo-liquidsoap/<script>.log",  # FIXME: Move to config
        "auth_command": here / "liquidsoap_auth.py",  # FIXME: Move to config
    }


def get_stream_config():
    """
    TODO: Move backoff logic to API client (rework api_client).
    """

    @backoff.on_exception(
        backoff.expo,
        (Timeout, ConnectionError),
        max_tries=10,
    )
    def call():
        api = ApiClient()
        payload = api.get_stream_setting()
        return payload["msg"]

    return call()
