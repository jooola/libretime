import sys
from pathlib import Path
from typing import Dict, List, Optional

from jinja2 import Template
from loguru import logger
from pydantic import BaseModel, ValidationError
from typing_extensions import Literal

here = Path(__file__).parent

entrypoint_template_path = here / "soap/main.liq.j2"
entrypoint_template: Template = Template(entrypoint_template_path.read_text())


class IcecastOutput(BaseModel):
    id: str
    enabled: bool = False

    # Meta
    name: str
    description: str = ""
    url: str = ""
    genre: str = "various"

    # Audio
    audio_type: Literal["ogg", "mp3"] = "ogg"
    audio_channels: Literal["stereo", "mono"] = "stereo"
    audio_bitrate: int = 256

    # Icecast
    icecast_protocol: Literal["http", "https"] = "http"
    icecast_host: str = "localhost"
    icecast_port: str = "8000"
    icecast_mount: str = "/main"

    # Icecast Auth
    icecast_admin_user: str = "admin"
    icecast_admin_password: str = "hackme"


class LiveInput(BaseModel):
    port: int = 8001
    mount: str = "/main"


class Config(BaseModel):
    icecast_outputs: Optional[List[IcecastOutput]]

    live_inputs: Optional[List[LiveInput]]
    live_inputs_listen_address: str = "0.0.0.0"

    log_filepath: Path = Path("liquidsoap.log")
    socket_filepath: Path = Path("liquidsoap.sock")
    run_filepath: Path = here / "soap/run.liq"
    vars_filepath: Path = Path("vars.json")

    prometheus_enabled: bool = False
    prometheus_listen_port: int = 9090


def generate_entrypoint(filepath: Path, data: dict) -> None:
    try:
        config = Config(**data)
    except ValidationError as error:
        logger.critical(error)
        sys.exit(1)

    filepath.write_text(entrypoint_template.render(**config.dict()))
