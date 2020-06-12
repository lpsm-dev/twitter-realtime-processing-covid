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
  if realtime:
    if realtime == "Consumer":
      logger.info(f"This is {realtime}...")
    if realtime == "Producer":
      logger.info(f"This is {realtime}...")
      track = [
        u"covid-19", u"corona",
        u"covid", u"corona virus",
        u"stay home", u"coronavirus",
        u"pandemic"
      ]
      twitter_streamer = TwitterStreamer()
      twitter_streamer.stream_tweets(track)
  else:
    logger.error("Error - missing Realtime type")
    sys.exit()
