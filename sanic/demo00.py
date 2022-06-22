# -*- coding: utf-8 -*-
# @Author  :   clumba
# @File    :   demo00.py
# @Time    :   2022/6/14 8:56
# file name: sanic_test.py
from sanic import Sanic
from sanic.response import json

app = Sanic(name="app")

@app.route('/')
async def test(request):
    msg = {'msg': 'Hello Sanic：本机'}
    return json(msg, ensure_ascii=False)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8889)