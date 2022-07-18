from queue import Queue as Pipe

from kombu import Connection, Exchange, Message, Queue
from kombu.mixins import ConsumerMixin
from loguru import logger

PLAYOUT_EXCHANGE = Exchange(
    name="playout",
    type="topic",
)

SCHEDULE_ROUTING_KEY = "playout.schedule"
SCHEDULE_QUEUE = Queue(
    name="playout.schedule",
    exchange=PLAYOUT_EXCHANGE,
    routing_key=SCHEDULE_ROUTING_KEY,
)

SOURCE_ROUTING_KEY = "playout.source"
SOURCE_QUEUE = Queue(
    name="playout.source",
    exchange=PLAYOUT_EXCHANGE,
    routing_key=SOURCE_ROUTING_KEY,
)

SETTING_ROUTING_KEY = "playout.setting"
SETTING_QUEUE = Queue(
    name="playout.setting",
    exchange=PLAYOUT_EXCHANGE,
    routing_key=SETTING_ROUTING_KEY,
)

RECORD_ROUTING_KEY = "playout.record"
RECORD_QUEUE = Queue(
    name="playout.record",
    exchange=PLAYOUT_EXCHANGE,
    routing_key=RECORD_ROUTING_KEY,
)


class MessageHandler(ConsumerMixin):
    """
    MessageHandler is a consumer that handle messages from RabbitMQ.
    """

    scheduler: Pipe

    def __init__(self, connection: Connection, scheduler: Pipe):
        self.connection = connection
        self.scheduler = scheduler

    def get_consumers(self, Consumer, channel):
        return [
            Consumer(queues=[SCHEDULE_QUEUE], callbacks=[self.on_schedule_message]),
            Consumer(queues=[SOURCE_QUEUE], callbacks=[self.on_source_message]),
            Consumer(queues=[SETTING_QUEUE], callbacks=[self.on_setting_message]),
            Consumer(queues=[RECORD_QUEUE], callbacks=[self.on_record_message]),
        ]

    def on_schedule_message(self, _body, message: Message):
        logger.debug(f"received: {message.payload}")
        self.scheduler.put(message.payload)
        message.ack()

    def on_source_message(self, _body, message: Message):
        logger.debug(f"received: {message.payload}")
        message.ack()

    def on_setting_message(self, _body, message: Message):
        logger.debug(f"received: {message.payload}")
        message.ack()

    def on_record_message(self, _body, message: Message):
        logger.debug(f"received: {message.payload}")
        message.ack()
