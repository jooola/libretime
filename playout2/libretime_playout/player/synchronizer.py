import math
from datetime import datetime
from queue import Queue
from threading import Thread

from loguru import logger


class Synchronizer(Thread):
    name = "synchronizer"

    def __init__(self):
        super().__init__()
        self.pushed_objects = {}
        self.current_prebuffering_stream_id = None
        self.queue_id = 0

        self.future_scheduled_queue = Queue()

    def main(self):
        loops = 0
        heartbeat_period = math.floor(30 / 2)

        media_schedule = None

        while True:
            try:
                media_schedule = self.queue.get(block=True)
            except Exception as e:
                logger.error(str(e))
                raise
            else:
                logger.debug(media_schedule)
                # separate media_schedule list into currently_playing and
                # scheduled_for_future lists
                currently_playing, scheduled_for_future = self.separate_present_future(
                    media_schedule
                )

                self.pypo_liquidsoap.verify_correct_present_media(currently_playing)
                self.future_scheduled_queue.put(scheduled_for_future)

            if loops % heartbeat_period == 0:
                logger.info("heartbeat")
                loops = 0
            loops += 1

    def separate_present_future(self, media_schedule):
        tnow = datetime.utcnow()

        present = []
        future = {}

        sorted_keys = sorted(media_schedule.keys())
        for mkey in sorted_keys:
            media_item = media_schedule[mkey]

            # Ignore track that already ended
            if media_item["end"] < tnow:
                logger.debug(f"ignoring ended media_item: {media_item}")
                continue

            diff_td = tnow - media_item["start"]
            diff_sec = self.date_interval_to_seconds(diff_td)

            if diff_sec >= 0:
                logger.debug(f"adding media_item to present: {media_item}")
                present.append(media_item)
            else:
                logger.debug(f"adding media_item to future: {media_item}")
                future[mkey] = media_item

        return present, future

    def push_on_time(self):
        time_until_next_play = None
        schedule_deque = deque()
        media_schedule = None

        while True:
            try:
                if time_until_next_play is None:
                    logger.info("waiting indefinitely for schedule")
                    media_schedule = self.queue.get(block=True)
                else:
                    logger.info(
                        "waiting %ss until next scheduled item" % time_until_next_play
                    )
                    media_schedule = self.queue.get(
                        block=True, timeout=time_until_next_play
                    )
            except Empty as e:
                # Time to push a scheduled item.
                media_item = schedule_deque.popleft()
                self.pypo_liquidsoap.play(media_item)
                if len(schedule_deque):
                    time_until_next_play = self.date_interval_to_seconds(
                        schedule_deque[0]["start"] - datetime.utcnow()
                    )
                    if time_until_next_play < 0:
                        time_until_next_play = 0
                else:
                    time_until_next_play = None
            else:
                logger.info("New schedule received: %s", media_schedule)

                # new schedule received. Replace old one with this.
                schedule_deque.clear()

                keys = sorted(media_schedule.keys())
                for i in keys:
                    schedule_deque.append(media_schedule[i])

                if len(keys):
                    time_until_next_play = self.date_interval_to_seconds(
                        media_schedule[keys[0]]["start"] - datetime.utcnow()
                    )

                else:
                    time_until_next_play = None
