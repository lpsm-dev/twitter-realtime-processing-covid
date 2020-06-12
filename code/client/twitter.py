# -*- coding: utf-8 -*-

from tweepy import OAuthHandler
from variables.general import logger
from dataclasses import dataclass, field
from typing import NoReturn, Text, Callable

@dataclass(init=True, repr=False)
class TwitterBase():
  consumer_key: Text = field(init=True, repr=False)
  consumer_secret: Text = field(init=True, repr=False)
  access_token: Text = field(init=True, repr=False)
  access_token_secret: Text = field(init=True, repr=False)

class TwitterAuthenticator(TwitterBase):

  def __init__(self,
      consumer_key: Text,
      consumer_secret: Text,
      access_token: Text,
      access_token_secret: Text) -> NoReturn:
    super().__init__(
      consumer_key,
      consumer_secret,
      access_token,
      access_token_secret
    )

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
