from os import execl
from pathlib import Path
from typing import Optional

import click
from libretime_shared.cli import cli_logging_options
from libretime_shared.config import DEFAULT_ENV_PREFIX
from libretime_shared.logging import level_from_name, setup_logger
from loguru import logger

from .entrypoint import generate_entrypoint
from .version import UnsupportedVersion, get_version, is_valid_version

here = Path(__file__).parent


config = {
    "icecast_outputs": [
        {
            "id": "main1",
            "enabled": True,
            "name": "Main ogg (256kbps)",
            # Audio
            "audio_type": "ogg",
            "audio_channels": "stereo",
            "audio_bitrate": 256,
            # Icecast
            "icecast_host": "localhost",
            "icecast_port": 8000,
            "icecast_mount": "/main.ogg",
            # Icecast Auth
            "icecast_admin_user": "admin",
            "icecast_admin_password": "admin",
        }
    ]
}


@click.command(context_settings={"auto_envvar_prefix": DEFAULT_ENV_PREFIX})
@cli_logging_options()
def cli(log_level: str, log_filepath: Optional[Path]) -> None:
    """
    Run liquidsoap.
    """
    log_level = level_from_name(log_level)
    setup_logger(log_level, log_filepath)

    version = get_version()
    if not is_valid_version(version):
        raise UnsupportedVersion(version)

    entrypoint_path = Path("./main.liq")
    generate_entrypoint(entrypoint_path, config)

    logger.debug(f"liquidsoap {version} using {entrypoint_path}")

    exec_args = [
        "/usr/bin/liquidsoap",
        "libretime-liquidsoap",
        "--verbose",
        str(entrypoint_path),
    ]

    if log_level.is_debug():
        exec_args.append("--debug")

    execl(*exec_args)
