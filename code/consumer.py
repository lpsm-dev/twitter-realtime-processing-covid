# -*- coding: utf-8 -*-

from json import loads
from core.consumer import TwitterConsumer
from variables.general import broker, logger, tweets_topic


# ==============================================================================
# GLOBAL
# ==============================================================================

consumer = TwitterConsumer(broker, tweets_topic).consumer

# ==============================================================================
# MAIN
# ==============================================================================

if __name__ == "__main__":
  if consumer.bootstrap_connected():
    logger.info("Connection okay.")
    for messagem in consumer:
      logger.info(messagem.value)
  else:
    logger.error("Failed to connect to service")
