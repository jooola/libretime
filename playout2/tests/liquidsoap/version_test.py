import pytest

from libretime_liquidsoap.version import is_valid_version, parse_version

LIQUIDSOAP_VERSION_RAW = """Liquidsoap 1.1.1
Copyright (c) 2003-2013 Savonet team
Liquidsoap is open-source software, released under GNU General Public License.
See <http://liquidsoap.fm> for more information.
"""


def test_parse_version():
    assert parse_version(LIQUIDSOAP_VERSION_RAW) == (1, 1, 1)


@pytest.mark.parametrize(
    "version, valid",
    [
        ("invalid data", False),
        ("Liquidsoap 1.1.0", False),
        ("Liquidsoap 1.1.1", True),
        ("Liquidsoap 1.4.4", True),
        ("Liquidsoap 2.0.0", False),
        ("Liquidsoap 2.0.2", False),
    ],
)
def test_is_valid_version(version, valid):
    assert is_valid_version(version) == valid
