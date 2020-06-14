# -*- coding: utf-8 -*-

import re
import emoji
from datetime import datetime
from typing import NoReturn, Text, Dict
from dataclasses import dataclass, field

from variables.general import logger

# ==============================================================================
# CLASS
# ==============================================================================

@dataclass(init=True, repr=True)
class TweetCleaner():
  remove_retweets: bool = field(init=True, repr=False, default=False)

  def remove_emoji(self, tweet: Text) -> Text:
    return re.sub(emoji.get_emoji_regexp(), r"", tweet)

  def filter_tweet(self, tweet: Dict) -> Dict:
    logger.info("Filter tweet information...")
    text = tweet["extended_tweet"]["full_text"] if "extended_tweet" in tweet else tweet["text"]
    return {
      "user_name": tweet["user"]["screen_name"],
      "followers": tweet["user"]["followers_count"],
      "friends": tweet["user"]["friends_count"],
      "text": self.remove_emoji(text),
      "data_collection": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
