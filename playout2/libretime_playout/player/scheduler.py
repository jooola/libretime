from datetime import datetime
from queue import Empty, Queue
from threading import Event, Thread
from typing import Any, Dict, List, Union

from loguru import logger
from pydantic import BaseModel


class _BaseSchedule(BaseModel):
    id: int  # Previously `row_id`
    url: str

    show_name: str

    start: datetime
    end: datetime


class FileSchedule(_BaseSchedule):
    metadata: Dict[str, Any]


class StreamSchedule(_BaseSchedule):
    pass


def ingest(items: List[Union[FileSchedule, StreamSchedule]]):
    """
    Ingest and dispatch a list of schedule.
    """
    pass


class Scheduler(Thread):
    name = "scheduler"
    queue: Queue
    stop: Event

    def __init__(self, stop: Event):
        super().__init__()
        self.queue = Queue()
        self.stop = stop

    def run(self):
        logger.info("starting scheduler")
        while not self.stop.is_set():
            try:
                ingest(self.queue.get(timeout=2))
            except Empty:
                pass

        logger.info("stopped scheduler")
