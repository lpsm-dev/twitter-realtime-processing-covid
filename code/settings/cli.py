# -*- coding: utf-8 -*-

from typing import NoReturn, Text
from argparse import ArgumentParser, RawTextHelpFormatter, ArgumentError

from constants.general import CLI

# ==============================================================================
# CLASS
# ==============================================================================

class CLIArguments:

  def __init__(self) -> NoReturn:
    self._parser = self._create_parser_object()
    self._adding_arguments()
    self.args = vars(self._parser.parse_args())

  @staticmethod
  def _create_parser_object() -> ArgumentParser:
    try:
      return ArgumentParser(
        description="Twitter realtime processing tweets covid-19 using kafka",
        prog="twitter-realtime-processing",
        epilog=CLI,
        formatter_class=RawTextHelpFormatter)
    except ArgumentError as error:
      print(f"Error when we create a parser object - {error}")

  def _adding_arguments(self) -> NoReturn:
    self._parser.add_argument("-r", "--realtime",
                                type=str,
                                metavar="<path>",
                                choices=["consumer", "producer"],
                                help="Type Realtime - Consumer or Producer")
    self._parser.add_argument("-v", "--version",
                                action="store_true",
                                help="Show Extracon version")
