from datetime import datetime, timedelta
from enum import Enum
from queue import Empty, Queue
from threading import Event, Thread
from typing import Any, Dict, List, Union

from pydantic import BaseModel

from .scheduler import FileSchedule, StreamSchedule


class _BaseEvent(BaseModel):
    schedule: Union[FileSchedule, StreamSchedule]
    start: datetime
    end: datetime


class FileEvent(_BaseEvent):
    metadata: Dict[str, Any]

    @classmethod
    def from_schedule(cls, item: FileSchedule) -> List["FileEvent"]:
        return [
            cls(
                schedule=item,
                start=item.start,
                end=item.end,
            )
        ]


class StreamAction(str, Enum):
    start_buffer = "start_buffer"
    start_output = "start_output"
    end_output = "end_output"
    end_buffer = "end_buffer"


class StreamEvent(_BaseEvent):
    action: StreamAction

    @classmethod
    def from_schedule(cls, item: StreamSchedule) -> List["StreamEvent"]:
        return [
            cls(
                schedule=item,
                start=item.start,
                end=item.start,
                action=StreamAction.start_buffer,
            ),
            cls(
                schedule=item,
                start=item.start,
                end=item.start,
                action=StreamAction.start_output,
            ),
            cls(
                schedule=item,
                start=item.end,
                end=item.end,
                action=StreamAction.end_output,
            ),
            cls(
                schedule=item,
                start=item.end,
                end=item.end,
                action=StreamAction.end_buffer,
            ),
        ]


class Dispatcher(Thread):
    """
    Build a stream of events from a schedule.
    """

    name = "dispatcher"
    queue: Queue
    stop: Event

    def __init__(self, queue: Queue, stop: Event):
        super().__init__()
        self.queue = queue
        self.stop = stop

    def run(self):
        while not self.stop.is_set():
            try:
                self.ingest(self.queue.get(timeout=2))
            except Empty:
                pass

    def ingest(self, items: List[Union[FileSchedule, StreamSchedule]]):
        """
        Ingest a schedule.
        """
        events = []
        for item in items:
            if isinstance(item, FileSchedule):
                events.extend(FileEvent.from_schedule(item))
            elif isinstance(item, StreamSchedule):
                events.extend(StreamEvent.from_schedule(item))

        now = datetime.utcnow()
        future = now + timedelta(days=1)

        str_current = now.isoformat(timespec="seconds")
        str_end = future.isoformat(timespec="seconds")
        for item in data:
            start = isoparse(item["starts"])
            start_key = start.strftime("%Y-%m-%d-%H-%M-%S")
            end = isoparse(item["ends"])
            end_key = end.strftime("%Y-%m-%d-%H-%M-%S")

            show_instance = self.services.show_instance_url(id=item["instance_id"])
            show = self.services.show_url(id=show_instance["show_id"])

            result[start_key] = {
                "start": start_key,
                "end": end_key,
                "row_id": item["id"],
                "show_name": show["name"],
            }
            current = result[start_key]
            if item["file"]:
                current["independent_event"] = False
                current["type"] = "file"
                current["id"] = item["file_id"]

                # current["fade_in"] = fade_in
                # current["fade_out"] = fade_out
                # current["cue_in"] = cue_in
                # current["cue_out"] = cue_out

                current["metadata"] = info
                current["uri"] = item["file"]
                current["replay_gain"] = info["replay_gain"]
                current["filesize"] = info["filesize"]
            elif item["stream"]:
                current["independent_event"] = True
                current["id"] = item["stream_id"]
                current["uri"] = info["url"]
                current["type"] = "stream_buffer_start"
                # Stream events are instantaneous
                current["end"] = current["start"]

                result[f"{start_key}_0"] = {
                    "id": current["id"],
                    "type": "stream_output_start",
                    "start": current["start"],
                    "end": current["start"],
                    "uri": current["uri"],
                    "row_id": current["row_id"],
                    "independent_event": current["independent_event"],
                }

                result[end_key] = {
                    "type": "stream_buffer_end",
                    "start": current["end"],
                    "end": current["end"],
                    "uri": current["uri"],
                    "row_id": current["row_id"],
                    "independent_event": current["independent_event"],
                }

                result[f"{end_key}_0"] = {
                    "type": "stream_output_end",
                    "start": current["end"],
                    "end": current["end"],
                    "uri": current["uri"],
                    "row_id": current["row_id"],
                    "independent_event": current["independent_event"],
                }

        return {"media": result}
