# -*- coding: utf-8 -*-

from json import dumps
from time import sleep
from typing import Dict, List, NoReturn, Text

from kafka import KafkaProducer
from kafka.errors import KafkaError
from variables.general import MAX_RETRIES, logger

# ==============================================================================
# CLASS
# ==============================================================================


class TwitterProducer:

    def __init__(self, broker: List) -> NoReturn:
        self.broker = broker
        self.producer = self.get()

    def get(self) -> KafkaProducer:
        retries = 0
        while retries <= MAX_RETRIES:
            try:
                logger.info(f"Getting kafka producer - Retries {retries}")
                return KafkaProducer(
                    bootstrap_servers=self.broker,
                    value_serializer=lambda value: dumps(value).encode("utf8"),
                    max_block_ms=10000000
                )
            except KafkaError:
                logger.warning(f"No broker available. Retrying {retries}")
                retries += 1
                sleep(3)

    def send_message(self, topic: Text, payload: Dict) -> NoReturn:
        self.producer.send(
            topic,
            value=payload
        )

    def close(self) -> NoReturn:
        self.producer.close()
