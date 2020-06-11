# -*- coding: utf-8 -*-

import logging
import coloredlogs
from typing import NoReturn, Text
from tools.os import OS
from settings.handlers import BaseFileHandler, ContextHandler

class SingletonLogger(type):

  _instances = {}

  def __call__(cls, *args, **kwargs):
    if cls not in cls._instances:
      cls._instances[cls] = super(
        SingletonLogger, cls
      ).__call__(*args, **kwargs)
    return cls._instances[cls]

class Log(OS, metaclass=SingletonLogger):

  LEVELS = ["CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG", "NOTSET"]

  def __init__(self, log_path: Text,
      log_file: Text,
      log_level: Text,
      logger_name: Text) -> NoReturn:
    self._log_path = log_path
    self._log_file = self.join_directory_with_file(self.log_path, log_file)
    self._log_level = log_level if log_level in self.LEVELS else "DEBUG"
    self._logger_name = logger_name
    self.formatter = "%(levelname)s - %(asctime)s - %(message)s - %(pathname)s - %(funcName)s"
    self.check_if_path_and_file_exist(self._log_path, self._log_file)
    self._logger = logging.getLogger(self.logger_name)
    self._logger.setLevel(self.log_level)
    self._base_configuration_log_colored()
    self._logger.addHandler(ContextHandler(
      BaseFileHandler()
    ).get_handler(
      log_file=self.log_file,
      log_level=self.log_level,
      formatter=self.formatter)
    )

  def _base_configuration_log_colored(self) -> coloredlogs.install:
    coloredlogs.install(level=self._log_level,
                        logger=self.logger,
                        fmt=self.formatter,
                        milliseconds=True)

  @property
  def log_path(self) -> Text:
    return self._log_path

  @property
  def log_file(self) -> Text:
    return self._log_file

  @property
  def log_level(self) -> Text:
    return self._log_level

  @property
  def logger_name(self) -> Text:
    return self._logger_name

  @property
  def logger(self) -> Text:
    return self._logger
