# -*- coding: utf-8 -*-

import sys
from colorama import init
init(strip=not sys.stdout.isatty())
from termcolor import cprint
from pyfiglet import figlet_format
from variables.general import realtime, vesion, logger
from constants.general import VERSION
from typing import NoReturn

# ==============================================================================
# FUNCTIONS
# ==============================================================================

def run() -> NoReturn:
  if vesion:
    print(VERSION)
    sys.exit()

  if realtime:
    cprint(figlet_format(realtime, font="starwars"), "white", attrs=["dark"])
    logger.info("Everything is Okay!")
    if realtime == "Consumer":
      logger.info("Consumer")
    if realtime == "Producer":
      logger.info("Producer")
  else:
    logger.error("Error - missing Realtime type")
    sys.exit()
