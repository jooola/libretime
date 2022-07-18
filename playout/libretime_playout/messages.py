from kombu.connection import Connection
from kombu.messaging import Exchange, Queue
from kombu.mixins import ConsumerMixin
from loguru import logger

from .player import PlayerHandler
from .scheduler import SchedulerHandler


class MessageHandler(ConsumerMixin):
    exchange = Exchange("playout", "direct", durable=True)

    player_queue = Queue("player", exchange=exchange, key="player.#")
    schedule_queue = Queue("scheduler", exchange=exchange, key="schedule.#")
    settings_queue = Queue("settings", exchange=exchange, key="settings.#")

    def __init__(self, connection: Connection):
        self.connection = connection

        self.player = PlayerHandler()
        self.scheduler = SchedulerHandler()

    def get_consumers(self, Consumer, channel):
        return [
            Consumer(
                queues=[self.player_queue],
                callbacks=[self.player.handle_message],
                accept=["application/json"],
            ),
            Consumer(
                self.schedule_queue,
                callbacks=[self.scheduler.handle_message],
                accept=["application/json"],
            ),
        ]
