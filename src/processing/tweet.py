# -*- coding: utf-8 -*-

import re
from dataclasses import dataclass
from datetime import datetime
from json import loads
from typing import Dict, Text

import emoji
from variables.general import logger

# ==============================================================================
# CLASS
# ==============================================================================

@dataclass(init=True, repr=True)
class TweetCleaner:

  def remove_emoji(self, tweet: Text) -> Text:
    emoji_expression = emoji.get_emoji_regexp()
    if emoji_expression:
      return re.sub(emoji_expression, r"", tweet)

  def get_tweet_text(self, tweet: Dict) -> Text:
    if "extended_tweet" in tweet:
      text = tweet["extended_tweet"]["full_text"]
    else:
      text = tweet["text"]
    return text

  def filter_tweet(self, tweet: Dict) -> Dict:
    logger.info("Filter tweet information...")
    tweet = loads(tweet)
    return {
      "user_name": tweet["user"]["screen_name"],
      "followers": tweet["user"]["followers_count"],
      "friends": tweet["user"]["friends_count"],
      "text": self.remove_emoji(self.get_tweet_text(tweet)),
      "data_collection": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
