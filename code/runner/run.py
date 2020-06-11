# -*- coding: utf-8 -*-

import sys
from colorama import init
init(strip=not sys.stdout.isatty())
from termcolor import cprint
from pyfiglet import figlet_format

# ==============================================================================
# FUNCTIONS
# ==============================================================================

def run() -> NoReturn:
  cprint(figlet_format("Extracon", font="starwars"), "white", attrs=["dark"])
