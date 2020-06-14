# -*- coding: utf-8 -*-

from time import sleep
from json import loads
from datetime import datetime
from typing import NoReturn, Text, Callable
from tweepy.streaming import StreamListener
from urllib3.exceptions import ProtocolError

from processing.tweet import TweetCleaner
from variables.general import logger, tweets_topic

# ==============================================================================
# CLASS
# ==============================================================================

class TwitterListener(StreamListener):

  def __init__(self, producer: Callable) -> NoReturn:
    self.producer = producer

  def on_connect(self) -> NoReturn:
    logger.info("You are now connected to twitter streaming API.")

  def on_data(self, data: Text) -> NoReturn:
    try:
      tweet = TweetCleaner(remove_retweets=False).filter_tweet(loads(data))
      logger.info("Send message to Kafka Producer...")
      self.producer.send_message(tweets_topic, tweet)
      logger.info("Sleeping 3 seconds...")
      sleep(3)
    except BaseException as error:
      logger.error(f"BaseException Twitter On Data - {error}")
    except Exception as error:
      logger.error(f"Exception Twitter On Data - {error}")
    except ProtocolError as error:
      logger.error(f"ProtocolError Twitter On Data - {error}")
    else:
      return True

  def on_error(self, status_code) -> bool:
    if status_code == 420:
      logger.error(f"Returning False on_data method in case rate limit occurs")
      return False
    logger.error(f"Error received in kafka producer - {status_code}")
    return True

  def on_timeout(self) -> bool:
    logger.error(f"Twitter timeout...")
    return True
