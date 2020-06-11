# -*- coding: utf-8 -*-

import sys
import logging
from pythonjsonlogger import jsonlogger
from abc import ABCMeta, abstractmethod
from typing import NoReturn, Text, List

class StrategyHandler(metaclass=ABCMeta):

  @abstractmethod
  def handler(self, *args, **kwargs) -> NoReturn:
    pass

class ContextHandler:

  def __init__(self, strategy: StrategyHandler) -> NoReturn:
    self._strategy = strategy

  @property
  def strategy(self) -> StrategyHandler:
    return self._strategy

  def get_handler(self, *args, **kwargs) -> NoReturn:
    return self._strategy.handler(*args, **kwargs)

class BaseFileHandler(StrategyHandler):

  @staticmethod
  def set_handler(file_handler, *args, **kwargs) -> NoReturn:
    file_handler.setLevel(kwargs["log_level"])
    file_handler.setFormatter(
      jsonlogger.JsonFormatter(kwargs["formatter"])
    )

  def handler(self, *args, **kwargs) -> logging.FileHandler:
    file_handler = logging.FileHandler(filename=kwargs["log_file"])
    self.set_handler(file_handler, *args, **kwargs)
    return file_handler

class BaseStreamHandler(StrategyHandler):

  @staticmethod
  def set_handler(stream_handler, *args, **kwargs) -> NoReturn:
    stream_handler.setLevel(kwargs["log_level"])
    stream_handler.setFormatter(
      jsonlogger.JsonFormatter(kwargs["formatter"])
    )

  def handler(self, *args, **kwargs) -> logging.StreamHandler:
    stream_handler = logging.StreamHandler(sys.stdout)
    self.set_handler(stream_handler, *args, **kwargs)
    return stream_handler
