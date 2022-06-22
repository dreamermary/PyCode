# -*- coding: utf-8 -*-
# @Author  :   clumba
# @File    :   run01.py
# @Time    :   2022/6/15 9:23

import sys
import os
# from sanic import BluePrint
from jinja2 import Environment,PackageLoader,select_autoescape
from config.config import Config
from sanic import  Sanic

sys.path.append('../') # 添加环境变量
from src.views import json_bp,html_bp,api_bp,redis_bp

'''
sanic 接收请求返回资源
    接收请求->路由&视图函数->jinja2模板渲染&返回视图
视图函数：服务的逻辑实现

bluepeint:模块化的编写不同类型的后台,不同模块自动附加前缀;
    不考虑命名问题,不用写重复前缀;
    路由根据特点(definedByYou)分割成一个蓝图

该文件中构建蓝图,可抽插式构建服务

'''

app = Sanic(__name__)
app.blueprint(json_bp)
app.blueprint(html_bp)
app.blueprint(api_bp)
app.blueprint(redis_bp)

if __name__ == "__main__":
    app.run(host='127.0.0.1',port=8889)




