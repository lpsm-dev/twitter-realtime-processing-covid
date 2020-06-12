# -*- coding: utf-8 -*-

from time import sleep
from datetime import datetime
from json import dumps, loads
from tweepy import Stream, API
from tweepy.streaming import StreamListener
from typing import NoReturn, List, Callable, Text

from core.producer import TwitterProducer
from clients.twitter import TwitterAuthenticator

from variables.general import (
  logger, tweets_topic, broker,
  twitter_consumer_key,
  twitter_consumer_secret,
  twitter_access_token,
  twitter_access_token_secret
)


from pprint import pprint

class TwitterStreamer():

  def __init__(self) -> NoReturn:
    self.twitter_autenticator = TwitterAuthenticator(
      twitter_consumer_key,
      twitter_consumer_secret,
      twitter_access_token,
      twitter_access_token_secret
    )

  def stream_tweets(self, track: List) -> NoReturn:
    auth = self.twitter_autenticator.authenticate_twitter()
    api = API(auth)
    listener = TwitterListener(api)
    stream = Stream(
      auth,
      listener
    )
    stream.filter(track=track)

class TwitterListener(StreamListener):

  def __init__(self, api: Callable):
    self.api = api
    self.producer = TwitterProducer(broker)

  def on_connect(self) -> NoReturn:
    logger.info("You are now connected to the Twitter streaming API.")

  def on_data(self, data: Text) -> NoReturn:
    try:
      parsed = loads(data)
      tweet = dumps({
        "user_name": parsed["user"]["screen_name"],
        "followers": parsed["user"]["followers_count"],
        "friends": parsed["user"]["friends_count"],
        "data_collection": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
      })
      logger.info("Send message to Kafka Producer...")
      self.producer.send_message(tweets_topic, tweet.encode("utf-8"))
      logger.info("Sleeping 3 seconds...")
      sleep(3)
    except BaseException as error:
      logger.error(f"BaseException Twitter On Data - {error}")
    except Exception as error:
      logger.error(f"Exception Twitter On Data - {error}")
    return True

  def on_error(self, status_code) -> bool:
    if status_code == 420:
      logger.error(f"Returning False on_data method in case rate limit occurs")
      return False
    logger.error(f"Error received in kafka producer - {status_code}")
    return True

  def on_timeout(self) -> bool:
    logger.warning(f"Twitter timeout...")
    return True
