# -*- coding: utf-8 -*-

import tweepy
from tweepy import Stream
from http.client import IncompleteRead
from typing import Callable, NoReturn, Text, List

from streamer.listener import TwitterListener
from variables.general import (
  twitter_consumer_key,
  twitter_consumer_secret,
  twitter_access_token,
  twitter_access_token_secret
)

class TwitterStreamer():

  def stream_tweets(self, track: List) -> NoReturn:
    auth = tweepy.OAuthHandler(twitter_consumer_key, twitter_consumer_secret)
    auth.set_access_token(twitter_access_token, twitter_access_token_secret)
    api = tweepy.API(auth)
    listener = TwitterListener(api)
    while True:
      try:
        stream = Stream(
          auth,
          listener
        )
        stream.filter(track=track)
      except IncompleteRead:
        continue
      except KeyboardInterrupt:
        stream.disconnect()
        break
