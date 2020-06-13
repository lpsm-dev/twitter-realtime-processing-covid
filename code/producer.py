# -*- coding: utf-8 -*-

from tweepy import Stream
from kafka import KafkaProducer
from http.client import IncompleteRead

from client.twitter import TwitterClient
from core.producer import TwitterProducer
from streamer.listener import TwitterListener
from variables.general import (
  broker, logger, twitter_consumer_key, twitter_consumer_secret,
  twitter_access_token, twitter_access_token_secret
)

# ==============================================================================
# GLOBAL
# ==============================================================================

producer = TwitterProducer(broker)

twitter_client = TwitterClient(
  twitter_consumer_key, twitter_consumer_secret,
  twitter_access_token, twitter_access_token_secret
)

# ==============================================================================
# MAIN
# ==============================================================================

if __name__ == "__main__":

  if producer.producer.bootstrap_connected():
    listener = TwitterListener(producer)
    while True:
      try:
        stream = Stream(
          twitter_client.twitter_client.auth,
          listener
        )
        stream.filter(
          track=[
            "covid", "corona",
            "pandemic", "covid-19",
            "virus", "corona virus"
          ]
        )
      except IncompleteRead:
        logger.info("I'm Here!")
        continue
      except KeyboardInterrupt:
        stream.disconnect()
        producer.producer.close()
        break
  else:
    logger.error("Failed to connect to service")
