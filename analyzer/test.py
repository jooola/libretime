from subprocess import CalledProcessError, run
from tempfile import SpooledTemporaryFile
from typing import Any, Dict
from subprocess import PIPE
from libretime_analyzer.pipeline._ffmpeg import _ffmpeg, FFMPEG


with SpooledTemporaryFile(max_size=50000) as tmp_fd:
    cmd = run(
        (
            FFMPEG,
            "-hide_banner",
            "-nostats",
            "-i",
            "tests/fixtures/s1.flac",
            "-acodec",
            "pcm_s16le",
            "-f",
            "wav",
            "-",
        ),
        check=True,
        stdout=tmp_fd,
        stderr=PIPE,
    )

    cmd = run(
        ("soundstretch", "stdin", "-bpm"),
        check=True,
        input=tmp_fd,
        stdout=PIPE,
        stderr=PIPE,
    )

    print(cmd.stdout)
