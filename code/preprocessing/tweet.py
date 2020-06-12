# -*- coding: utf-8 -*-

import re
import emoji
from datetime import datetime
from typing import NoReturn, Text, Dict
from variables.general import logger

class TweetCleaner(object):

  def __init__(self, remove_retweets=False) -> NoReturn:
    self.remove_retweets = remove_retweets

  def give_emoji_free_text(self, text: Text) -> Text:
    allchars = [string for string in text]
    emoji_list = [string for string in allchars if string in emoji.UNICODE_EMOJI]
    return " ".join([string for string in text.split()
      if not any(value in string for value in emoji_list)])

  def get_claned_retweet_text(self, text: Text) -> Text:
    if re.match(r"RT @[_A-Za-z0-9]+:", text):
      if self.remove_retweets: return ""
      retweet_info = text[:text.index(":") + 2]
      text = text[text.index(":")+ 2:]
    else:
      retweet_info = ""
    return retweet_info

  def get_cleaned_text(self, text: Text) -> Text:
    try:
      cleaned_text = text.replace("\n", "").replace('\"','').replace('\'','').replace('-',' ')
      retweet_info = self.get_claned_retweet_text(cleaned_text)
      cleaned_text = re.sub(r"@[a-zA-Z0-9_]+", "", (retweet_info + cleaned_text)).strip()
      cleaned_text = re.sub(r"RT\s:\s", "", cleaned_text).lstrip()
      cleaned_text = cleaned_text[::] if cleaned_text[0] != " " else cleaned_text[1::]
      cleaned_text = self.give_emoji_free_text(cleaned_text)
      cleaned_text = re.sub(r"http\S+", "", cleaned_text)
      cleaned_text = re.sub(r"https\S+", "", cleaned_text)
      return cleaned_text
    except Exception as error:
      logger.error(f"Error get cleaned tweet text - {error}")

  def filter_tweet(self, tweet: Dict) -> Dict:
    try:
      if "extended_tweet" in tweet:
        text = tweet["extended_tweet"]["full_text"]
      else:
        text = tweet["text"]
      tweet = {
        "id": tweet["id"],
        "name": tweet["user"]["name"],
        "screen_name": tweet["user"]["screen_name"],
        "followers_count": tweet["user"]["followers_count"],
        "friends_count": tweet["user"]["friends_count"],
        "text": self.get_cleaned_text(text).encode("utf-8"),
        "location": tweet["user"]["location"] if tweet["user"]["location"] else "",
        "data_collection": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
      }
    except Exception as error:
      logger.error(f"Error when we filter the tweet information - {error}")
    else:
      logger.info(f"Sucess get, filter and clean tweet: {tweet}")
      return tweet
