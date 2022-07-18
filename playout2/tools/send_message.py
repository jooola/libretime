#!/usr/bin/env python3

from datetime import datetime, timedelta

from kombu import Connection, Producer

from libretime_playout.config import Config
from libretime_playout.message_handler import PLAYOUT_EXCHANGE, SCHEDULE_ROUTING_KEY
from music import files

now = datetime.utcnow()

message = []
i = 0
for file in files:
    message.append(
        {
            "id": i,
            "start": now + timedelta(minutes=i),
            "end": now + timedelta(minutes=1 + i),
            "url": f"file://{file.resolve()}",
            "show_name": "Testing",
        }
    )
    i += 1

with Connection(Config().rabbitmq.url) as conn:
    with conn.channel() as channel:
        producer = Producer(
            exchange=PLAYOUT_EXCHANGE,
            channel=channel,
        )
        producer.publish(
            message,
            exchange=PLAYOUT_EXCHANGE,
            routing_key=SCHEDULE_ROUTING_KEY,
        )
