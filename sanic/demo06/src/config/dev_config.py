# -*- coding: utf-8 -*-
# @Author  :   clumba
# @File    :   dev_config.py
# @Time    :   2022/6/14 17:09
from .config import Config
import os

class DevConfig(Config):
    DEBUG = True
    AUTH = {
        "Api-Key": os.getenv('OWLLOOK_API_KEY', "1167c19cd0546a82fbc534f5e93423d5")
    }