# -*- coding: utf-8 -*-

import sys
from colorama import init
init(strip=not sys.stdout.isatty())
from termcolor import cprint
from pyfiglet import figlet_format

from typing import NoReturn
from variables.general import realtime, version, logger
from constants.general import VERSION

# ==============================================================================
# FUNCTION PRODUCER
# ==============================================================================

def producer() -> NoReturn:
  from streamer.twitter import TwitterStreamer

  track = [
    "covid-19", "corona",
    "covid", "corona virus",
    "stay home", "coronavirus",
    "pandemic"
  ]

  twitter_streamer = TwitterStreamer()
  twitter_streamer.stream_tweets(track)

# ==============================================================================
# FUNCTION CONSUMER
# ==============================================================================

def consumer() -> NoReturn:
  from json import loads
  from kafka import KafkaConsumer
  from variables.general import  broker, tweets_topic

  consumer = KafkaConsumer(
    tweets_topic,
    group_id="group1",
    bootstrap_servers=[broker]
  )

  frases = ""
  for messagem in consumer:
    texto = loads(messagem.value.decode("utf-8"))
    print(texto)
    frases = frases + texto.get("text", "No Found")
    print(frases)


# ==============================================================================
# FUNCTIONS RUN
# ==============================================================================

def run() -> NoReturn:
  cprint(figlet_format(realtime, font="starwars"), "white", attrs=["dark"])
  logger.info("Running twitter realtime processing tweets covid-19 using kafka!")
