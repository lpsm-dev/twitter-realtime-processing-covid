# -*- coding: utf-8 -*-

from time import sleep
from datetime import datetime
from json import dumps, loads
from kafka import KafkaProducer
from tweepy.streaming import StreamListener
from typing import NoReturn, Callable, Text
from urllib3.exceptions import ProtocolError

from variables.general import logger, tweets_topic, broker

class TwitterListener(StreamListener):

  def __init__(self, api: Callable) -> NoReturn:
    self.api = api
    self.producer = KafkaProducer(bootstrap_servers=[broker])

  def on_connect(self) -> NoReturn:
    logger.info("You are now connected to the Twitter streaming API.")

  def on_data(self, data: Text) -> NoReturn:
    try:
      parsed = loads(data)
      if "extended_tweet" in parsed:
        text = parsed["extended_tweet"]["full_text"]
      text = parsed["text"]
      tweet = dumps({
        "user_name": parsed["user"]["screen_name"],
        "followers": parsed["user"]["followers_count"],
        "friends": parsed["user"]["friends_count"],
        "text": text,
        "data_collection": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
      })
      logger.info(f"Send message to kafka producer on {tweets_topic} topic...")
      self.producer.send(tweets_topic, value=tweet.encode("utf-8"))
      logger.info("Waiting 3 seconds...")
      sleep(3)
    except BaseException as error:
      logger.error(f"BaseException twitter listener - {error}")
    except Exception as error:
      logger.error(f"Exception twitter listener - {error}")
    except ProtocolError as error:
      logger.error(f"ProtocolError twitter listener - {error}")
    else:
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
