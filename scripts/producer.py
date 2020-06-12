# -*- coding: utf-8 -*-

import tweepy
from time import sleep
from tweepy import Stream
from json import dumps, loads
from datetime import datetime
from kafka import KafkaProducer
from http.client import IncompleteRead
from tweepy.streaming import StreamListener
from typing import Callable, NoReturn, Text
from urllib3.exceptions import ProtocolError

# ==============================================================================
# GLOBAL
# ==============================================================================

TWITTER_CONSUMER_KEY = "ZYsGMoOFEGsZZ9zyCWEXy3C5H"
TWITTER_CONSUMER_SECRET = "102hsQ3Z1FYPlA2HNg8Vwc0wudKQQfn1l726r7Q3eH6ZchZz4R"
TWITTER_ACCESS_TOKEN = "1065019734167613440-riMkzW2vmo68FNYQlPXrOdHFG2gCOf"
TWITTER_ACCESS_TOKEN_SECRET = "eTHwBEHdcHxSZiI54euMDU78wyElZJ7iX2CJMK17zmrO5"

broker, topico = "localhost:9092", "dados-tweets"

# ==============================================================================
# CLASS
# ==============================================================================

class TwitterListener(StreamListener):

  def __init__(self, api: Callable):
    self.api = api
    self.producer = KafkaProducer(bootstrap_servers=[broker])

  def on_connect(self) -> NoReturn:
    print("You are now connected to the Twitter streaming API.")

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
      print("Send message to Kafka Producer...")
      self.producer.send(topico, value=tweet.encode("utf-8"))
      print("Sleeping 3 seconds...")
      sleep(3)
    except BaseException as error:
      print(f"BaseException Twitter On Data - {error}")
    except Exception as error:
      print(f"Exception Twitter On Data - {error}")
    except ProtocolError as error:
      print(f"ProtocolError Twitter On Data - {error}")
    else:
      return True

  def on_error(self, status_code) -> bool:
    if status_code == 420:
      print(f"Returning False on_data method in case rate limit occurs")
      return False
    print(f"Error received in kafka producer - {status_code}")
    return True

  def on_timeout(self) -> bool:
    print(f"Twitter timeout...")
    return True

auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
listener = TwitterListener(api)

while True:
  try:
    stream = Stream(
      auth,
      listener
    )
    stream.filter(track=["covid", "corona", "pandemic", "covid-19", "virus", "corona virus"])
  except IncompleteRead:
    continue
  except KeyboardInterrupt:
    stream.disconnect()
    break
