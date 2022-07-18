from pathlib import Path
from socket import AF_UNIX, SOCK_STREAM, socket
from threading import Lock
from time import sleep
from typing import Tuple, Union

from loguru import logger
from typing_extensions import Literal

from .version import UnsupportedVersion, is_valid_version, parse_version


class LiquidsoapSocket:
    """
    A gateway to communicate with a running liquidsoap server.

    Communication go though a unix socket file, socket path is provided with `path`.
    """

    path: Path
    sock: socket
    lock: Lock  # TODO: Do we really need a lock ?

    def __init__(self, path: Union[Path, str]):
        self.path = Path(path)
        self.sock = socket(AF_UNIX, SOCK_STREAM)
        self.lock = Lock()

    def connect(self):
        """
        Connect to the liquidsoap socket file.
        """
        # TODO: How long can a connection be open without communication ? What is the unix socket timeout ?
        # Keeping the connection open would make the communication less versbose
        logger.debug(f"connecting to {self.path}")
        self.lock.acquire()
        self.sock.connect(str(self.path))

    def close(self):
        """
        Close the connection to liquidsoap.
        """
        logger.debug(f"closing connection to {self.path}")
        self.write("exit")

        self.sock.close()
        self.lock.release()

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, _exc_type, _exc_value, _traceback):
        self.close()

    def write(self, msg: str):
        """
        Write a message to liquidsoap.
        """
        buffer = msg.encode(encoding="utf-8")
        buffer += b"\n"

        logger.trace(f"sending {buffer!r}")
        self.sock.sendall(buffer)

    CHUNK_SIZE = 4096
    CHUNK_EOF = b"END"

    def read(self) -> str:
        """
        Read a message from liquidsoap.
        """
        chunks = []
        while True:
            chunk = self.sock.recv(self.CHUNK_SIZE)
            chunk = chunk.replace(b"\r\n", b"\n")
            eof_index = chunk.find(self.CHUNK_EOF)

            if eof_index >= 0:
                chunk = chunk[:eof_index]
                chunks.append(chunk)
                break

            chunks.append(chunk)
        buffer = b"".join(chunks)
        logger.trace(f"received {buffer!r}")

        return buffer.strip().decode("utf-8")

    def version(self) -> Tuple[int, int, int]:
        """
        Get the liquidsoap version.
        """
        with self:
            self.write("version")
            resp = self.read()
            return parse_version(resp)

    def sanity_check(self) -> None:
        """
        Try to connect to liquidsoap and assert the running version is supported.

        This function will loop until a connection to liquidsoap is established.
        """
        while True:
            try:
                version = self.version()

                if is_valid_version(version):
                    break

                raise UnsupportedVersion(f"liquidsoap {version} is not supported")
            except FileNotFoundError:
                logger.warning("trying again in 5 seconds!")
                sleep(5)

    def queues_remove(self, *queues: int) -> None:
        with self:
            for queue_id in queues:
                self.write(f"queues.{queue_id}_skip")

    def queue_push(self, queue_id: int, entry: str, show_name: str) -> None:
        with self:
            self.write(f"queues.{queue_id}_skip")
            self.write(f"{queue_id}.push {entry}")
            self.write(f"vars.show_name {show_name}")

    def web_stream_stop_buffer(self) -> None:
        with self:
            self.write("http.stop")
            self.write("dynamic_source.id -1")

    def web_stream_start_buffer(self, schedule_id: int, uri: str) -> None:
        with self:
            self.write(f"dynamic_source.id {schedule_id}")
            self.write(f"http.restart {uri}")

    def web_stream_get_id(self) -> None:
        with self:
            self.write("dynamic_source.get_id")
            return self.read().splitlines()[0]

    def web_stream_stop(self) -> None:
        with self:
            self.write("dynamic_source.output_stop")

    def web_stream_start(self) -> None:
        with self:
            self.write("streams.scheduled_play_start")
            self.write("dynamic_source.output_start")

    def source_disconnect(self, name: Literal["master_dj", "live_dj"]) -> None:
        command_map = {
            "master_dj": "master_harbor.stop",
            "live_dj": "live_dj_harbor.stop",
        }
        with self:
            self.write(command_map[name])

    def source_switch_status(self, name: str, status: Literal["start", "stop"]) -> None:
        with self:
            self.write(f"streams.{name}_{status}")
