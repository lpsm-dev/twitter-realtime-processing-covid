# -*- coding: utf-8 -*-

from os import environ
from typing import Text

# ==============================================================================
# CLASS
# ==============================================================================

class Config:

  @staticmethod
  def get_env(env: Text) -> Text:
    try:
      return environ.get(env)
    except KeyError as error:
      print(f"Key Error: {error}")
