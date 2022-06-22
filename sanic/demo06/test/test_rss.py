# -*- coding: utf-8 -*-
# @Author  :   clumba
# @File    :   test_rss.py
# @Time    :   2022/6/21 16:25

import ujson
import pytest
import uvloop

import settting




async def test_http_rss(test_cli):
    data = setting.rss_data()
    response = await test_cli.post(
        '/v1/post/rss',data=ujson.dumps())
    resp_json = await response.json()
    assert resp_json['status'] == 1

async def test_grpc_rss():
    pass