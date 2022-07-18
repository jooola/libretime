from typing import Optional

from libretime_shared.config import BaseConfig
from pydantic import Extra, conlist

from .input import Inputs
from .output import Output


class Config(BaseConfig, extra=Extra.forbid):
    inputs: Inputs
    outputs: Optional[conlist(Output, min_items=1, max_items=4)]
