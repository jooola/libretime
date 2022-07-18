import sys
import time
from datetime import datetime
from pathlib import Path
from signal import SIGINT, SIGTERM, signal
from threading import Event
from typing import Optional

import click
from kombu import Connection
from libretime_shared.config import DEFAULT_ENV_PREFIX
from libretime_shared.cli import cli_config_options, cli_logging_options
from libretime_shared.logging import level_from_name, setup_logger
from loguru import logger

from .config import CACHE_DIR, RECORD_DIR, Config
from .message_handler import MessageHandler
from .player.scheduler import Scheduler


@click.command(context_settings={"auto_envvar_prefix": DEFAULT_ENV_PREFIX})
@cli_logging_options()
@cli_config_options()
def cli(log_level: str, log_filepath: Optional[Path], config_filepath: Optional[Path]):
    """
    Run playout.
    """
    setup_logger(level_from_name(log_level), log_filepath)
    config = Config(filepath=config_filepath)

    logger.info(f"timezone: {time.tzname}")
    logger.info(f"utc time: {datetime.utcnow()}")

    try:
        logger.info("creating directories")
        for dir_path in [CACHE_DIR, RECORD_DIR]:
            dir_path.mkdir(exist_ok=True)
    except OSError as exception:
        logger.error(exception)
        sys.exit(1)

    stop = Event()

    def stop_handler(_signum, _frame):
        logger.info("stopping...")
        message_handler.should_stop = True
        stop.set()

    signal(SIGINT, stop_handler)
    signal(SIGTERM, stop_handler)

    logger.info("starting scheduler")
    scheduler = Scheduler(stop)
    scheduler.start()

    with Connection(config.rabbitmq.url, heartbeat=5) as connection:
        logger.info("starting message handler")
        message_handler = MessageHandler(connection, scheduler.queue)
        message_handler.run()
