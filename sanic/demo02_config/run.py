# -*- coding: utf-8 -*-
# @Author  :   clumba
# @File    :   run01.py
# @Time    :   2022/6/14 16:43

from sanic import Sanic
from sanic.response import text
from config import CONFIG

app = Sanic(name='app')

@app.route('/')
async def test(request):
    return text('hello world')

if __name__ == "__main__":
    app.run(host='127.0.0.1',port=8889,debug=CONFIG)