import shutil
from pathlib import Path

import pytest

from libretime_analyzer.pipeline.context import Context

from .fixtures import fixtures_path

AUDIO_FILENAME = "s1-stereo-tagged.mp3"
AUDIO_FILE = fixtures_path / AUDIO_FILENAME
AUDIO_IMPORT_DEST = f"Test Artist/Test Album/{AUDIO_FILENAME}"


@pytest.fixture()
def dest_dir(tmp_path):
    yield tmp_path


@pytest.fixture()
def src_dir(tmp_path):
    shutil.copy(AUDIO_FILE, tmp_path)
    yield tmp_path


def context_factory(filepath: Path):
    return Context(
        filepath=filepath,
        original_filename="",
        storage_url="",
        callback_api_key="",
        callback_url="",
    )
