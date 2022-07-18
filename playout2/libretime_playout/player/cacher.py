from queue import Empty, Queue
from threading import Event, Thread
from urllib.parse import urlsplit

from loguru import logger

from .scheduler import FileSchedule


class Cacher(Thread):
    name = "cacher"
    queue: Queue
    stop: Event

    def __init__(self, queue: Queue, stop: Event):
        super().__init__()
        self.queue = queue
        self.stop = stop

    def run(self):
        while not self.stop.is_set():
            try:
                self.cache(self.queue.get(timeout=2))
            except Empty:
                pass

    def cache(self, item: FileSchedule):
        """
        Copy item from storage to the local cache.
        """

        # Check if item should be cached

        # Check if file is already cached

        # Cache the file
        url = urlsplit(item.url)
        if url.scheme == "file":
            self.cache_from_file(item)
        elif url.scheme in ("http", "https"):
            self.cache_from_http(item)
        else:
            raise ValueError("invalid schema")

    def cache_from_http(self, item: FileSchedule):
        pass

    def cache_from_file(self, item: FileSchedule):
        pass
