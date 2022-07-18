from pathlib import Path

from libretime_playout.liquidsoap.config import Config

here = Path(__file__).parent


def test_config():
    config = Config(filepath=here / "config.yml")
    print(config.json(indent=4))
    assert False
