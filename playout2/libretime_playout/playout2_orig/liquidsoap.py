import re
import telnetlib
import time

from . import pure
from .timeout import ls_timeout

LIQUIDSOAP_MIN_VERSION = "1.1.1"


@ls_timeout
def liquidsoap_get_info(telnet_lock, host, port, logger):
    logger.debug("Checking to see if Liquidsoap is running")
    try:
        telnet_lock.acquire()
        tn = telnetlib.Telnet(host, port)
        msg = "version\n"
        tn.write(msg.encode("utf-8"))
        tn.write(b"exit\n")
        response = tn.read_all().decode("utf-8")
    except Exception as e:
        logger.error(e)
        return None
    finally:
        telnet_lock.release()

    return get_liquidsoap_version(response)


def get_liquidsoap_version(version_string):
    m = re.match(r"Liquidsoap (\d+.\d+.\d+)", version_string)

    if m:
        return m.group(1)
    else:
        return None

    if m:
        current_version = m.group(1)
        return pure.version_cmp(current_version, LIQUIDSOAP_MIN_VERSION) >= 0
    return False


def liquidsoap_startup_test(telnet_lock, ls_host, ls_port):

    liquidsoap_version_string = liquidsoap_get_info(
        telnet_lock, ls_host, ls_port, logger
    )
    while not liquidsoap_version_string:
        logger.warning(
            "Liquidsoap doesn't appear to be running!, " + "Sleeping and trying again"
        )
        time.sleep(1)
        liquidsoap_version_string = liquidsoap_get_info(
            telnet_lock, ls_host, ls_port, logger
        )

    while pure.version_cmp(liquidsoap_version_string, LIQUIDSOAP_MIN_VERSION) < 0:
        logger.warning(
            "Liquidsoap is running but in incorrect version! "
            + "Make sure you have at least Liquidsoap %s installed"
            % LIQUIDSOAP_MIN_VERSION
        )
        time.sleep(1)
        liquidsoap_version_string = liquidsoap_get_info(
            telnet_lock, ls_host, ls_port, logger
        )

    logger.info("Liquidsoap version string found %s" % liquidsoap_version_string)
