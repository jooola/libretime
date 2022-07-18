import signal
import sys
from datetime import datetime
from pathlib import Path
from queue import Queue
from threading import Lock
from time import sleep, tzname
from typing import Optional

from libretime_api_client.version1 import AirtimeApiClient as ApiClient
from libretime_shared.app import AbstractApp
from libretime_shared.config import DEFAULT_CONFIG_FILEPATH
from loguru import logger

from .config import Config
from .liquidsoap import liquidsoap_startup_test
from .listenerstat import ListenerStat
from .pypofetch import PypoFetch
from .pypofile import PypoFile
from .pypoliquidsoap import PypoLiquidsoap
from .pypomessagehandler import PypoMessageHandler
from .pypopush import PypoPush
from .recorder import Recorder


class Playout(AbstractApp):
    name = "playout"
    config_filepath: Optional[Path] = None

    def __init__(self, config_filepath, **kwargs):
        super().__init__(**kwargs)
        self.config_filepath = config_filepath or DEFAULT_CONFIG_FILEPATH
        self.config = Config(filepath=self.config_filepath)

        self.api_client = ApiClient()

        while not self.sanity_check():
            sleep(5)

        success = False
        while not success:
            try:
                self.api_client.register_component("pypo")
                success = True
            except Exception as error:
                logger.error(error)
                sleep(10)

    def sanity_check(self) -> bool:
        return self.api_client.is_server_compatible()

    def shutdown_handler(self, _signum, _frame):
        logger.info(f"stopping {self.name}")
        sys.exit(0)

    def run(self):
        signal.signal(signal.SIGINT, self.shutdown_handler)

        logger.info(f"Timezone: {tzname}")
        logger.info(f"UTC time: {datetime.utcnow()}")

        telnet_lock = Lock()
        liquidsoap_host = self.config.playout.liquidsoap_host
        liquidsoap_port = self.config.playout.liquidsoap_port

        liquidsoap_startup_test(telnet_lock, liquidsoap_host, liquidsoap_port)

        fetch_queue = Queue()
        recorder_queue = Queue()
        push_queue = Queue()
        media_queue = Queue()

        pypo_liquidsoap = PypoLiquidsoap(
            logger,
            telnet_lock,
            liquidsoap_host,
            liquidsoap_port,
        )

        message_handler_thread = PypoMessageHandler(
            fetch_queue,
            recorder_queue,
            self.config.rabbitmq,
        )
        message_handler_thread.daemon = True
        message_handler_thread.start()

        file_thread = PypoFile(media_queue, self.config.playout)
        file_thread.daemon = True
        file_thread.start()

        fetch_thread = PypoFetch(
            fetch_queue,
            push_queue,
            media_queue,
            telnet_lock,
            pypo_liquidsoap,
            self.config,
        )
        fetch_thread.daemon = True
        fetch_thread.start()

        pp = PypoPush(push_queue, telnet_lock, pypo_liquidsoap, self.config.playout)
        pp.daemon = True
        pp.start()

        recorder = Recorder(recorder_queue)
        recorder.daemon = True
        recorder.start()

        stat = ListenerStat(self.config)
        stat.daemon = True
        stat.start()

        # Just sleep the main thread, instead of blocking on pf.join().
        # This allows CTRL-C to work!
        while True:
            sleep(1)
