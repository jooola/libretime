from typing import List, Protocol

from loguru import logger

from .analyze_cuepoint import analyze_cuepoint
from .analyze_metadata import analyze_metadata
from .analyze_playability import analyze_playability
from .analyze_replaygain import analyze_replaygain
from .context import Context, Status
from .exceptions import PipelineError, StepError
from .organise_file import organise_file


class Step(Protocol):
    @staticmethod
    def __call__(ctx: Context) -> Context:
        ...


def run_pipeline(ctx: Context) -> Context:
    """
    Run each pipeline step on the incoming audio file.

    If a `Step` raise a `StepError`, the pipeline will stop and the error will be
    reported back to the API.

    If a `Step` raise a `PipelineError`, the pipeline will stop and the analyzer
    reject the message. User should take action to fix any `PipelineError`, such as
    missing executables or else.
    """
    if not ctx.filepath.is_file():
        raise PipelineError(f"invalid or missing file {ctx.filepath}")

    try:
        ctx = analyze_playability(ctx)
        ctx = analyze_metadata(ctx)
        ctx = analyze_cuepoint(ctx)
        ctx = analyze_replaygain(ctx)
        ctx = organise_file(ctx)

        ctx.status = Status.SUCCEED

    except StepError as exception:
        ctx.status = Status.FAILED
        ctx.error = str(exception)
        logger.warning(exception)

    return ctx
