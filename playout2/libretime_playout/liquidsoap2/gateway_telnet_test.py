from unittest import mock

import pytest


@pytest.mark.parametrize(
    "response, expected",
    [
        ("invalid data", (0, 0, 0)),
        ("Liquidsoap 1.4.4", (1, 4, 4)),
    ],
)
def test_liquidsoap_gateway_version(session_mock, liquidsoap, response, expected):
    session_mock.read_all.return_value = response
    assert liquidsoap.version() == expected
    session_mock.write.assert_called_once_with("version")


def test_liquidsoap_gateway_sanity_check(session_mock, liquidsoap):
    session_mock.read_all.return_value = "Liquidsoap 1.4.4"
    liquidsoap.sanity_check()
    session_mock.write.assert_called_once_with("version")


def test_liquidsoap_gateway_sanity_check_invalid_version(session_mock, liquidsoap):
    session_mock.read_all.return_value = "Liquidsoap 2.0.2"
    with pytest.raises(UnsupportedLiquidsoapVersion):
        liquidsoap.sanity_check()
    session_mock.write.assert_called_once_with("version")


def test_liquidsoap_gateway_queues_remove(session_mock, liquidsoap):
    liquidsoap.queues_remove(1, 2, 3)
    session_mock.write.assert_has_calls(
        [
            mock.call("queues.1_skip"),
            mock.call("queues.2_skip"),
            mock.call("queues.3_skip"),
        ]
    )
