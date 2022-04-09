from pathlib import Path

import pytest

from libretime_analyzer.pipeline.analyze_metadata import (
    InvalidFile,
    InvalidMimeType,
    analyze_metadata,
)

from ..fixtures import FILE_INVALID_DRM, FILE_INVALID_TXT, FILES_TAGGED


@pytest.mark.parametrize(
    "filepath,metadata",
    map(lambda i: (i.path, i.metadata), FILES_TAGGED),
)
def test_analyze_metadata(filepath: Path, metadata: dict):
    found = analyze_metadata(str(filepath), {})

    assert len(found["md5"]) == 32
    del found["md5"]

    # Handle filesize
    assert found["filesize"] < 3e6  # ~3Mb
    assert found["filesize"] > 1e5  # 100Kb
    del found["filesize"]

    # Handle track formatted length
    assert metadata["length"] in found["length"]
    del metadata["length"]
    del found["length"]

    # mp3,ogg,flac files does not support comments yet
    if not filepath.suffix == ".m4a":
        if "comment" in metadata:
            del metadata["comment"]

    assert found == metadata


@pytest.mark.parametrize(
    "filepath,exception,match",
    [
        (FILE_INVALID_DRM, InvalidMimeType, "invalid mime type: audio/x-ms-wma"),
        (FILE_INVALID_TXT, InvalidFile, f"no metadata in {FILE_INVALID_TXT}"),
    ],
)
def test_analyze_metadata_invalid_mime_type(filepath, exception, match):
    with pytest.raises(exception, match=match):
        analyze_metadata(str(filepath), {})


def test_compute_md5():
    assert compute_md5(FILE_INVALID_TXT) == "4d5e4b1c8e8febbd31fa9ce7f088beae"
