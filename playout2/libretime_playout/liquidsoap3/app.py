from os import PathLike, execl
from pathlib import Path

from loguru import logger
from lt.shared.app import AbstractApp

from .config import compat_generate_config, generate_config, get_stream_config
from .utils import (
    CalledProcessError,
    ExecutableNotFound,
    get_version,
    is_valid_version,
    run_liquidsoap,
)

here = Path(__file__).parent


class App(AbstractApp):
    name = "liquidsoap"
    name_verbose = "Liquidsoap"

    def run(self):
        try:
            version = get_version()
        except (CalledProcessError, ExecutableNotFound) as error:
            logger.error(error)
            return 1

        if not is_valid_version(version):
            logger.error(f"unsupported liquidsoap version {version}")
            return 1

        # TODO: Make this an option
        config_path = Path("/etc/airtime/liquidsoap.cfg")

        dirty_config = get_stream_config()
        config = compat_generate_config(dirty_config)
        config_path.write_text(generate_config(config))

        script_file = here / f"{version}/ls_script.liq"

        run_liquidsoap("--check", script_file)

        args = ["liquidsoap", "--verbose", "--force-start"]
        if self.log_level.is_debug():
            args.append("--debug")

        logger.info(f"Running '{script_file}' with 'liquidsoap {version}'.")

        execl(*args, script_file)
