# -*- coding: utf-8 -*-

from http.client import IncompleteRead
from typing import Callable, List, NoReturn, Text

import tweepy
from client.twitter import TwitterClient
from core.producer import TwitterProducer
from streamer.listener import TwitterListener
from tweepy import Stream
from variables.general import (broker, logger, twitter_access_token,
                               twitter_access_token_secret,
                               twitter_consumer_key, twitter_consumer_secret)

# ==============================================================================
# CLASS
# ==============================================================================


class TwitterStreamer:

    def __init__(self) -> NoReturn:
        self.producer = TwitterProducer(broker)
        self.listener = TwitterListener(self.producer)
        self.twitter_client = TwitterClient(
            twitter_consumer_key, twitter_consumer_secret,
            twitter_access_token, twitter_access_token_secret
        )

    def _stream(self,
                languages=["en"],
                track=None
                ) -> Stream:
        stream = Stream(
            self.twitter_client.twitter_client.auth,
            self.listener
        )
        if track:
            stream.filter(
                track=track,
                languages=languages
            )
        else:
            stream.filter(
                languages=languages
            )
        return stream

    def stream_tweets(self, languages: List, track=None) -> NoReturn:
        if self.producer.producer.bootstrap_connected():
            while True:
                try:
                    stream = self._stream(languages, track)
                except IncompleteRead:
                    logger.info("I'm Here!")
                    continue
                except KeyboardInterrupt:
                    stream.disconnect()
                    self.producer.producer.close()
                    break
        else:
            logger.error("Failed to connect to service")
