import re
from contextlib import contextmanager
from socket import timeout as SocketTimeoutError
from threading import Lock
from time import sleep
from typing import Any, Dict, Literal, Tuple

from loguru import logger


class Socket:
    def write(self, *messages: str):
        for message in messages:
            logger.trace(message)
            super().write(f"{message}\n".encode())

    def read_all(self) -> str:
        response = super().read_all().decode("utf-8")
        logger.trace(response)
        return response


class UnsupportedLiquidsoapVersion(Exception):
    """
    Raised when liquidsoap version is not supported
    """


class LiquidsoapGateway:
    lock: Lock
    host: str
    port: int
    timeout: int

    def __init__(self, host: str, port: int = 0, timeout: int = 5):
        self.lock = Lock()
        self.host = host
        self.port = port
        self.timeout = timeout

    @contextmanager
    def session(self):
        with self.lock:
            try:
                with Telnet(
                    self.host,
                    port=self.port,
                    timeout=self.timeout,
                ) as connection:
                    yield connection
                    connection.write("exit")
                    response = connection.read_all()
                    logger.trace(response)

            except SocketTimeoutError as exception:
                logger.error(
                    f"could not open connection to "
                    f"liquidsoap {self.host}:{self.port}: {exception}"
                )
                raise exception

    def _parse_version(self, version_string: str) -> Tuple[int, int, int]:
        match = LIQUIDSOAP_VERSION_RE.search(version_string)

        if match is None:
            return (0, 0, 0)
        return (int(match.group(1)), int(match.group(2)), int(match.group(3)))
