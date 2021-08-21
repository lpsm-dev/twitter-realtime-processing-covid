# -*- coding: utf-8 -*-

import sys
from os import path, makedirs
from typing import NoReturn, Text

# ==============================================================================
# CLASS
# ==============================================================================

class OS:

  @classmethod
  def check_if_is_dir(cls, directory: Text) -> bool:
    return True if path.isdir(directory) else False

  @classmethod
  def check_if_is_file(cls, file: Text) -> bool:
    return True if path.isfile(file) else False

  @classmethod
  def join_directory_with_file(cls,
    directory: Text,
    file: Text
  ) -> Text:
    return str(path.join(directory, file))

  @classmethod
  def create_directory(cls, directory: Text) -> NoReturn:
    try:
      makedirs(directory)
    except OSError:
      print(f"OSError in create the directory {directory}")

  @classmethod
  def create_file(cls, file: Text) -> NoReturn:
    with open(file, mode="w"): pass

  def check_if_path_and_file_exist(self,
    directory: Text,
    file: Text,
    creation=True
  ) -> NoReturn:
    if self.check_if_is_dir(directory):
      if not self.check_if_is_file(file):
        if creation:
          self.create_file(file)
        else:
          raise Exception(f"File {file} not exist")
    else:
      self.create_directory(directory)
      self.create_file(file)
