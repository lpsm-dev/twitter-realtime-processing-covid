# -*- coding: utf-8 -*-

import sys
from colorama import init
init(strip=not sys.stdout.isatty())
from termcolor import cprint
from pyfiglet import figlet_format
from typing import NoReturn

from constants.general import VERSION
from variables.general import realtime, version, broker, logger, tweets_topic

from core.consumer import TwitterConsumer
from streamer.twitter import TwitterStreamer

# ==============================================================================
# FUNCTIONS
# ==============================================================================

def run() -> NoReturn:
  cprint(figlet_format(realtime, font="starwars"), "white", attrs=["dark"])
  logger.info("Running twitter realtime processing!")

  if version:
    print(VERSION)
    sys.exit()

  if realtime.lower() == "consumer":
    logger.info(f"This is {realtime}...")
    consumer = TwitterConsumer(broker, tweets_topic).consumer
    if consumer.bootstrap_connected():
      logger.info("Connection okay.")
      for messagem in consumer:
        logger.info(messagem.value)
    else:
      logger.error("Failed to connect to service")

  if realtime.lower() == "producer":
    logger.info(f"This is {realtime}...")
    track = [
      "covid", "corona",
      "pandemic", "covid-19",
      "virus", "corona virus"
    ]
    languages = ["en", "pt"]
    TwitterStreamer().stream_tweets(languages, track)
