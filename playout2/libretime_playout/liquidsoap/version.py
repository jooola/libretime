import re
from subprocess import run
from typing import NamedTuple, Union

LIQUIDSOAP_VERSION_RE = re.compile(r"Liquidsoap (\d+).(\d+).(\d+)")


class Version(NamedTuple):
    major: int
    minor: int
    patch: int

    def __str__(self) -> str:
        return f"{self.major}.{self.minor}.{self.patch}"


LIQUIDSOAP_MIN_VERSION = Version(2, 0, 0)
LIQUIDSOAP_MAX_VERSION = Version(2, 1, 0)


class UnsupportedVersion(Exception):
    """ "
    Trying to run an unsupported version of liquidsoap.
    """

    def __init__(self, version: Version) -> None:
        super().__init__(f"liquidsoap {version} is not supported!")


def parse_version(version: str) -> Version:
    match = LIQUIDSOAP_VERSION_RE.search(version)

    if match is None:
        return Version(0, 0, 0)
    return Version(int(match.group(1)), int(match.group(2)), int(match.group(3)))


def is_valid_version(version: Union[str, Version]) -> bool:
    if isinstance(version, str):
        version = parse_version(version)

    return LIQUIDSOAP_MIN_VERSION <= version <= LIQUIDSOAP_MAX_VERSION


def get_version() -> Version:
    cmd = run(
        ("liquidsoap", "--version"),
        text=True,
        capture_output=True,
        check=True,
    )
    return parse_version(cmd.stdout)
