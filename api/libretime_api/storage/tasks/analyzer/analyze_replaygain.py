from subprocess import CalledProcessError

from libretime_analyzer.pipeline.exceptions import PipelineError

from ...models import File
from ._ffmpeg import compute_replaygain, probe_replaygain


def analyze_replaygain(file_id: int):
    """
    Extracts the Replaygain loudness normalization factor of a track using ffmpeg.
    """
    file = File.objects.get(id=file_id)

    try:
        # First probe for existing replaygain metadata.
        track_gain = probe_replaygain(file.filepath)
        if track_gain is not None:
            ctx.metadata["replay_gain"] = track_gain
            return ctx
    except (CalledProcessError, FileNotFoundError) as exception:
        raise PipelineError(
            f"could not probe replaygain for {ctx.filepath}"
        ) from exception

    try:
        track_gain = compute_replaygain(ctx.filepath)
        if track_gain is not None:
            ctx.metadata["replay_gain"] = track_gain
    except (CalledProcessError, FileNotFoundError) as exception:
        raise PipelineError(
            f"could not compute replaygain for {ctx.filepath}"
        ) from exception

    return ctx
