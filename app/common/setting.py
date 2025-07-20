# coding: utf-8
from pathlib import Path

# change DEBUG to False if you want to compile the code to exe
DEBUG = "__compiled__" not in globals()


YEAR = 2025
AUTHOR = "GH OSA-QEFT开发小组"
VERSION = "v0.0.1"
APP_NAME = "QEFT"


CONFIG_FOLDER = Path('config').absolute()
CONFIG_FILE = CONFIG_FOLDER / "config.json"
