from kombu.message import Message
from loguru import logger


class PlayerHandler:
    def __init__(self):
        pass

    def handle_message(self, body: dict, message: Message):
        message.ack()
