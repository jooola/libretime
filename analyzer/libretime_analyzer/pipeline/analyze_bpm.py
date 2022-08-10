from subprocess import CalledProcessError, run
from tempfile import SpooledTemporaryFile, TemporaryFile
from typing import Any, Dict
from subprocess import PIPE
from ._ffmpeg import _ffmpeg, FFMPEG


def analyze_bpm(filepath: str, metadata: Dict[str, Any]):
    """
    Extracts the BPM for a track using ffmpeg and soundstretch.
    """

    # Ignore if bpm already present or file longer that 15 minutes
    if metadata.get("bpm") or metadata.get("length_seconds") > 60 * 15:
        return metadata

    with TemporaryFile() as tmp_fd:
        cmd = run(
            (
                FFMPEG,
                "-hide_banner",
                "-nostats",
                "-i",
                filepath,
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

    # result = run(
    #     ["soundstretch", tmp_file, "-bpm"],
    #     capture_output=True,
    #     universal_newlines=True,
    #     check=True,
    # )

    # track_bpm_match = re.search(
    #     r"Detected BPM rate ([0-9]+\.[0-9]+)",
    #     result.stderr,
    # )

    # if track_bpm_match:
    #     print(float(track_bpm_match.group(1)))

    #     try:
    #         track_gain = _ffmpeg(filepath)
    #         if track_gain is not None:
    #             metadata["replay_gain"] = track_gain
    #     except (CalledProcessError, OSError):
    #         pass

    # return metadata

    # result = run(
    #     ["ffmpeg -i $file -acodec pcm_s16le -f wav -"],
    #     capture_output=True,
    #     universal_newlines=True,
    #     check=True,
    # )
    # result.check_returncode()

    # result = run(
    #     ["soundstretch", tmp_file, "-bpm"],
    #     capture_output=True,
    #     universal_newlines=True,
    #     check=True,
    # )

    # track_bpm_match = re.search(
    #     r"Detected BPM rate ([0-9]+\.[0-9]+)",
    #     result.stderr,
    # )

    # if track_bpm_match:
    #     print(float(track_bpm_match.group(1)))
