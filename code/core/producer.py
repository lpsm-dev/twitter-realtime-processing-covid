# -*- coding: utf-8 -*-

from time import sleep
from json import dumps
from kafka import KafkaProducer
from kafka.errors import KafkaError
from typing import NoReturn, Text, List, Dict

from variables.general import logger

class TwitterProducer():

  MAX_RETRIES = 100

  def __init__(self, broker: List) -> NoReturn:
    self.broker = broker
    self.producer = self.get_producer()

  def get_producer(self) -> KafkaProducer:
    retries = 1
    while retries <= self.MAX_RETRIES:
      try:
        logger.info(f"Getting Kafka Producer - Retries {retries}")
        producer = KafkaProducer(
          bootstrap_servers=self.broker,
          value_serializer = lambda value: dumps(value).encode("utf8"),
          max_block_ms=10000000
        )
        return producer
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
