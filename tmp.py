# -*- coding: utf-8 -*-
# @Author  :   clumba
# @File    :   tmp.py
# @Time    :   2022/6/22 11:36

import requests

proxies = {
    "http": "http://127.0.0.1:7890",
    "https": "http://127.0.0.1:7890",
}

res = requests.get('https://www.google.com.hk/',proxies=proxies,)
print(res.text)


