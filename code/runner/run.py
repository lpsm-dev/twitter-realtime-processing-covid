# -*- coding: utf-8 -*-

from variables.general import (broker, logger, realtime, tweets_topic, version,
                               yml)
from termcolor import cprint
from streamer.twitter import TwitterStreamer
from pyfiglet import figlet_format
from core.consumer import TwitterConsumer
from constants.general import VERSION
from typing import NoReturn
import sys

from colorama import init

init(strip=not sys.stdout.isatty())


# ==============================================================================
# FUNCTIONS
# ==============================================================================


def producer() -> NoReturn:
    logger.info(f"This is {realtime}...")
    track = [
        "covid", "corona",
        "pandemic", "covid-19",
        "virus", "corona virus"
    ]
    languages = ["en", "pt"]
    TwitterStreamer().stream_tweets(languages, track)


def consumer() -> NoReturn:
    logger.info(f"This is {realtime}...")
    consumer = TwitterConsumer(broker, tweets_topic).consumer
    if consumer.bootstrap_connected():
        logger.info("Connection okay.")
        for messagem in consumer:
            logger.info(messagem.value)
    else:
        logger.error("Failed to connect to service")


def run() -> NoReturn:
    cprint(figlet_format(realtime, font="starwars"), "white", attrs=["dark"])
    logger.info("Running twitter realtime processing!")

    if version:
        print(VERSION)
        sys.exit()

    if realtime.lower() == "consumer":
        consumer()

    if realtime.lower() == "producer":
        producer()
