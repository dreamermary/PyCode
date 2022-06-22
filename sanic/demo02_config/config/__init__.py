# -*- coding: utf-8 -*-
# @Author  :   clumba
# @File    :   __init__.py.py
# @Time    :   2022/6/14 17:09

'''
实现项目的环境(生产环境/开发环境)配置：
从系统环境变量中获取参数,在__init__中根据参数加载配置文件,在app中调用；

os.environ.get

'''

import os

def load_config():
    mode = os.environ.get("MODE","DEV")

    try:
        if mode == "PRO":
            from .pro_config import ProConfig
            return ProConfig
        if mode == "DEV":
            from .dev_config import DevConfig
            return DevConfig
        else:
            from .dev_config import DevConfig
            return DevConfig
    except ImportError:
        from .config import Config
        return Config

CONFIG = load_config()



