from pathlib import Path
from subprocess import Popen
from time import sleep

import pytest
from libretime_shared.logging import TRACE, setup_logger

from libretime_liquidsoap.gateway import LiquidsoapSocket

here = Path(__file__).parent
gateway_script = here / "gateway_test.liq"

setup_logger(TRACE)


@pytest.fixture(scope="session")
def liq_socket(tmp_path_factory):
    tmp_path: Path = tmp_path_factory.mktemp(__name__)

    socket_path = tmp_path / "liquidsoap.sock"
    with Popen(
        (
            "/usr/bin/liquidsoap",
            "--verbose",
            str(gateway_script),
            "--",
            str(socket_path),
        )
    ) as process:
        while not socket_path.exists():
            sleep(0.5)

        sock = LiquidsoapSocket(path=socket_path)
        with sock:
            yield sock

        process.terminate()


def test_liquidsoap_gateway_version(liq_socket: LiquidsoapSocket):
    for _ in range(2):
        liq_socket.write("version")
        found = liq_socket.read()
        assert found == "Liquidsoap 2.0.2"


LIQUIDSOAP_HELP = """Available commands:
| dummy.metadata
| dummy.remaining
| dummy.skip
| exit
| help [<command>]
| list
| quit
| request.alive
| request.all
| request.metadata <rid>
| request.on_air
| request.resolving
| request.trace <rid>
| uptime
| var.get
| var.list
| var.set <name> = <value>
| version

Type "help <command>" for more information."""


def test_liquidsoap_gateway_help(liq_socket: LiquidsoapSocket):
    liq_socket.write("help")
    found = liq_socket.read()
    assert found == LIQUIDSOAP_HELP


def test_liquidsoap_gateway_var_get(liq_socket: LiquidsoapSocket):
    liq_socket.write("var.get var1")
    found = liq_socket.read()
    assert found == "false"


def test_liquidsoap_gateway_var_set(liq_socket: LiquidsoapSocket):
    liq_socket.write("var.set var1 = true")
    found = liq_socket.read()
    assert found == "Variable var1 set."

    liq_socket.write("var.get var1")
    found = liq_socket.read()
    assert found == "true"
