# -*- coding: utf-8 -*-

from time import sleep
from datetime import datetime
from json import dumps, loads
from kafka import KafkaProducer
from typing import NoReturn, Text
from tweepy.streaming import StreamListener
from urllib3.exceptions import ProtocolError

from variables.general import logger, tweets_topic, broker

class TwitterListener(StreamListener):

  def __init__(self) -> NoReturn:
    self.producer = KafkaProducer(
      bootstrap_servers=[broker],
      value_serializer=lambda value: dumps(value).encode("utf-8"),
      max_block_ms=10000000
    )

  def on_connect(self) -> NoReturn:
    logger.info("You are now connected to the Twitter streaming API.")

  def on_data(self, data: Text) -> NoReturn:
    try:
      parsed = loads(data)
      tweet = {
        "user_name": parsed[u"user"][u"screen_name"],
        "followers": parsed[u"user"][u"followers_count"],
        "friends": parsed[u"user"][u"friends_count"],
        "text": parsed[u"extended_tweet"][u"full_text"] if "extended_tweet" in parsed else parsed[u"text"],
        "data_collection": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
      }
    except BaseException as error:
      logger.error(f"BaseException twitter listener - {error}")
    except Exception as error:
      logger.error(f"Exception twitter listener - {error}")
    except ProtocolError as error:
      logger.error(f"ProtocolError twitter listener - {error}")
    except (KeyboardInterrupt, SystemExit):
      raise
    else:
      logger.info(f"Send message to kafka producer on {tweets_topic} topic...")
      self.producer.send(tweets_topic, value=tweet)
      self.producer.flush()
      logger.info("Waiting 3 seconds...")
      sleep(3)
      return True

  def on_error(self, status_code: int) -> bool:
    if status_code == 420:
      logger.error("Error received twitter listener - on_error status code 420")
      return False
    logger.error(f"Error received twitter listener - on_error status code {status_code}")
    return True

  def on_timeout(self) -> bool:
    logger.error(f"Error received twitter listener - on_timeout...")
    return True
