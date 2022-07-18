from datetime import datetime
from enum import Enum
from typing import Any, Dict, Literal, Union

from pydantic import BaseModel


class Schedulee:
    pass
    # schedule=  {
    #     "media": [
    #     $schedule_item = [
    #         'id' => $media_id,
    #         'type' => 'file',
    #         'metadata' => $fileMetadata,
    #         'row_id' => $item['id'],
    #         'uri' => $uri,
    #         'fade_in' => Application_Model_Schedule::WallTimeToMillisecs($item['fade_in']),
    #         'fade_out' => Application_Model_Schedule::WallTimeToMillisecs($item['fade_out']),
    #         'cue_in' => Application_Common_DateHelper::CalculateLengthInSeconds($item['cue_in']),
    #         'cue_out' => Application_Common_DateHelper::CalculateLengthInSeconds($item['cue_out']),
    #         'start' => $start,
    #         'end' => $end,
    #         'show_name' => $item['show_name'],
    #         'replay_gain' => $replay_gain,
    #         'independent_event' => $independent_event,
    #         'filesize' => $filesize,
    #     ];
    #     ]
    # }


class Media(BaseModel):
    kind: Literal["file", "stream"]

    id: int
    uri: str


class MediaFile(Media):
    kind = Literal["file"]

    metadata: Dict[str, Any]


class MediaStream(Media):
    kind = Literal["file"]


class Schedule(BaseModel):
    id: int  # Previous `row_id`
    media: Union[MediaFile, MediaStream]
    show_name: str


class StreamStatus(str, Enum):
    start = "start"
    stop = "stop"


class StreamBuffer(BaseModel):
    start: datetime
    end: datetime
    position: int  # Previous `row_id`
    status: StreamStatus
    independent_event: bool
    media_uri: str  # Previous `uri`


class StreamOutput(StreamBuffer):
    media_id: int  # Previous `id`
    show_name: str


class HarborKickStatus(str, Enum):
    kick_out = "kick_out"
    switch_off = "switch_off"


class HarborKick(BaseModel):
    start: datetime
    end: datetime
    status: HarborKickStatus


# $data['media'][$kick_start]['start'] = $kick_start;
# $data['media'][$kick_start]['end'] = $kick_start;
# $data['media'][$kick_start]['event_type'] = 'kick_out';
# $data['media'][$kick_start]['type'] = 'event';
# $data['media'][$kick_start]['independent_event'] = true;

# $data['media'][$switch_start]['start'] = $switch_start;
# $data['media'][$switch_start]['end'] = $switch_start;
# $data['media'][$switch_start]['event_type'] = 'switch_off';
# $data['media'][$switch_start]['type'] = 'event';
# $data['media'][$switch_start]['independent_event'] = true;
