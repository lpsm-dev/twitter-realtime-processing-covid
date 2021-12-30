# -*- coding: utf-8 -*-

from datetime import datetime
from time import sleep
from typing import Callable, NoReturn, Text

from processing.tweet import TweetCleaner
from tweepy.streaming import StreamListener
from urllib3.exceptions import ProtocolError
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
            tweet = TweetCleaner().filter_tweet(data)
            logger.info("Send message to kafka producer...")
            self.producer.send_message(tweets_topic, tweet)
            logger.info("Sleeping 3 seconds...")
            sleep(3)
        except Exception as error:
            logger.error(f"Exception Twitter on data - {error}")
        except ProtocolError as error:
            logger.error(f"ProtocolError Twitter on data - {error}")
        else:
            return True

    def on_error(self, status_code) -> bool:
        if status_code == 420:
            logger.error(
                f"Returning False on_data method in case rate limit occurs")
            return False
        logger.error(f"Error received in kafka producer - {status_code}")
        return True

    def on_timeout(self) -> bool:
        logger.error(f"Twitter timeout...")
        return True
