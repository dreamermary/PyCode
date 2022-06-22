# -*- coding: utf-8 -*-
# @Author  :   clumba
# @File    :   config.py
# @Time    :   2022/6/14 17:09
import os

class Config():
    '''
    Basic config
    '''
    TIMEZONE = 'Asia/Shanghai'
    BASE_DIR = os.path.dirname(os.path.dirname(__file__)) # ../demo2
