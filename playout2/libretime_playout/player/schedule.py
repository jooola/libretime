from datetime import datetime
from enum import Enum
from typing import Any, Union

from pydantic import BaseModel

from .schedule import Schedule


class Event(BaseModel):
    kind: str


class UpdateStationName(BaseModel):
    station_name: str


class UpdateStationNameEvent(BaseModel):
    kind = "update_station_name"
    payload: UpdateStationName


class SourceStatus(str, Enum):
    on = "on"
    off = "off"


class SwitchSource(BaseModel):
    source_name: str
    status: SourceStatus


class SwitchSourceEvent(BaseModel):
    kind = "switch_source"
    payload: SwitchSource


class ResetLiquidsoapBootstrapEvent(BaseModel):
    kind = "reset_liquidsoap_bootstrap"


class UpdateScheduleEvent(BaseModel):
    kind = "update_schedule"
    payload: Schedule
