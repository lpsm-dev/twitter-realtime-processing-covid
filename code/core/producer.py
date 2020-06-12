# -*- coding: utf-8 -*-

from time import sleep
from json import dumps
from kafka import KafkaProducer
from typing import NoReturn, Text, List, Dict
from kafka.errors import KafkaError, NoBrokersAvailable
from variables.general import logger

class TwitterProducer():

  MAX_RETRIES = 100

  def __init__(self, broker: List) -> NoReturn:
    self.broker = broker
    self.producer = self.get_producer()

  def get_producer(self):
    retries = 1
    while retries <= self.MAX_RETRIES:
      try:
        logger.info(f"Getting Kafka Producer - Retries {retries}")
        producer = KafkaProducer(
          bootstrap_servers=self.broker,
          max_block_ms=10000000
        )
        return producer
      except KafkaError:
        logger.warning(f"No broker available. Retrying {retries}")
        retries += 1
        sleep(1)

  def check_connection(self):
    if not self.producer.bootstrap_connected():
      logger.error("Producer bootstrap bad connection")

  def send_message(self, topic: Text, payload: Dict):
    self.check_connection()
    self.producer.send(topic, value=payload)

  def close(self) -> NoReturn:
    self.producer.close()
