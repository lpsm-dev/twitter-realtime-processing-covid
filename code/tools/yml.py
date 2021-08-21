# -*- coding: utf-8 -*-

import yaml
from typing import NoReturn, Dict

from tools.os import OS

# ==============================================================================
# CLASS
# ==============================================================================

class YML(OS):

  def __init__(self, file="values.yml", path="/usr/src/code") -> NoReturn:
    self.check_if_path_and_file_exist(path, file, creation=False)
    if file.endswith(".yaml") or file.endswith(".yml"):
      self.file = self.join_directory_with_file(path, file)
    else:
      raise Exception("We need a YML File")

  def get_content(self) -> Dict:
    try:
      with open(self.file) as file:
        try:
          content = yaml.load(file, Loader=yaml.FullLoader)
        except Exception:
          raise ValueError(f"Incorrect YAML syntax in file {self.file}!")
    except IOError:
      print("Yaml configuration not found.")
    except yaml.parser.ParserError:
      print("Invalid Yaml.")
    else:
      return content if content else {}
