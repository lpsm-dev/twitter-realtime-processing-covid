# -*- coding: utf-8 -*-

import sys
from colorama import init
init(strip=not sys.stdout.isatty())
from termcolor import cprint
from pyfiglet import figlet_format
from variables.general import realtime, vesion, logger
from constants.general import VERSION
from typing import NoReturn
from streamer.twitter import TwitterStreamer

# ==============================================================================
# FUNCTIONS
# ==============================================================================

def run() -> NoReturn:
  cprint(figlet_format(realtime, font="starwars"), "white", attrs=["dark"])
  logger.info("Running twitter realtime processing!")

  if vesion:
    print(VERSION)
    sys.exit()

  if realtime == "Producer":
    logger.info(f"This is {realtime}...")
    track = [
      "covid-19", "corona",
      "covid", "corona virus",
      "stay home", "coronavirus",
      "pandemic"
    ]
    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(track)

  elif realtime == "Consumer":
    logger.info(f"This is {realtime}...")
