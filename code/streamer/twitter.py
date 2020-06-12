# -*- coding: utf-8 -*-

from json import dumps, loads
from datetime import datetime
from clients.twitter import TwitterAuthenticator
from tweepy.streaming import StreamListener
from tweepy import Stream, API, OAuthHandler

from core.producer import TwitterProducer
from time import sleep

from variables.general import (
  logger, tweets_topic, broker,
  twitter_consumer_key,
  twitter_consumer_secret,
  twitter_access_token,
  twitter_access_token_secret
)

class TwitterStreamer():

  def __init__(self):
    self.twitter_autenticator = TwitterAuthenticator(
      twitter_consumer_key,
      twitter_consumer_secret,
      twitter_access_token,
      twitter_access_token_secret
    )

  def stream_tweets(self, track):
    auth = self.twitter_autenticator.authenticate_twitter()
    api = API(auth)
    listener = TwitterListener(api)
    stream = Stream(
      auth,
      listener
    )
    stream.filter(track=track)

class TwitterListener(StreamListener):

  def __init__(self, api):
    self.api = api
    self.producer = TwitterProducer(broker)

  def on_data(self, data):
    tweet = data.encode("utf-8")
    logger.info(tweet)
    self.producer.send_message(tweets_topic, tweet)
    sleep(3)
    return True

  def on_error(self, status):
    if status == 420:
      return False
    logger.info(status)

  def on_timeout(self):
    logger.info(f"Twitter timeout...")
    return True
