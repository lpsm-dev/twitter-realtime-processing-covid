# -*- coding: utf-8 -*-

from json import loads
from time import sleep
from typing import List, NoReturn, Text

from kafka import KafkaConsumer
from kafka.errors import KafkaError
from variables.general import MAX_RETRIES, logger

# ==============================================================================
# CLASS
# ==============================================================================


class TwitterConsumer:

    def __init__(self, broker: List, topic: Text) -> NoReturn:
        self.broker = broker
        self.topic = topic
        self.consumer = self.get()

    def get(self) -> KafkaConsumer:
        retries = 0
        while retries <= MAX_RETRIES:
            try:
                logger.info(f"Getting kafka consumer - Retries {retries}")
                return KafkaConsumer(
                    self.topic,
                    group_id="group1",
                    bootstrap_servers=self.broker,
                    value_deserializer=lambda messagem: loads(
                        messagem.decode("utf-8"))
                )
            except KafkaError:
                logger.warning(f"No broker available. Retrying {retries}")
                retries += 1
                sleep(3)
