# -*- coding: utf-8 -*-

from dataclasses import dataclass, field
from typing import NoReturn, Text, Callable
from tweepy import OAuthHandler, API
from tweepy.error import TweepError, RateLimitError
from variables.general import logger

@dataclass(init=True, repr=False)
class TwitterBase(object):
  consumer_key: Text = field(init=True, repr=False)
  consumer_secret: Text = field(init=True, repr=False)
  access_token: Text = field(init=True, repr=False)
  access_token_secret: Text = field(init=True, repr=False)

class TwitterAuthenticator(TwitterBase):

  def __init__(self, consumer_key: Text,
      consumer_secret: Text,
      access_token: Text,
      access_token_secret: Text) -> NoReturn:
    super().__init__(consumer_key,
                      consumer_secret,
                      access_token,
                      access_token_secret)

  def authenticate_twitter(self) -> OAuthHandler:
    auth = OAuthHandler(
      self.consumer_key,
      self.consumer_secret
    )
    auth.set_access_token(
      self.access_token,
      self.access_token_secret
    )
    return auth

class TwitterClient(TwitterAuthenticator):

  def __init__(self, consumer_key: Text,
      consumer_secret: Text,
      access_token: Text,
      access_token_secret: Text) -> NoReturn:
    super().__init__(consumer_key,
                      consumer_secret,
                      access_token,
                      access_token_secret)
    self.auth = self.authenticate_twitter()
    self.twitter_client = self.get_twitter_client()

  def get_twitter_client(self) -> Callable:
    twitter_client = API(
      self.auth,
      wait_on_rate_limit=True,
      wait_on_rate_limit_notify=True
    )
    try:
      logger.info("Checking Twitter credentials")
      twitter_client.verify_credentials()
    except RateLimitError as error:
      logger.error(f"Tweepy RateLimitError - {error}")
    except TweepError as error:
      logger.error(f"Tweepy TweepError - {error}")
    except Exception as error:
      logger.error(f"Error general exception - {error}")
    else:
      logger.info("Successful Twitter Authentication!")
      return twitter_client
