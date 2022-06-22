# -*- coding: utf-8 -*-
# @Author  :   clumba
# @File    :   rss_html.py.py
# @Time    :   2022/6/15 10:50
import sys
from sanic import Sanic,Blueprint
from sanic.response import json, text, html
from feedparser import parse
from jinja2 import Environment, PackageLoader, select_autoescape
import os

from src.config import CONFIG
from src.tools.mid_decorator import auth_params

from json import loads as json_load

'''
POST/GET:参数验证
'''
api_bp = Blueprint('rss_api',url_prefix='v1') # name,prefix

# url中的字符串作为参数
@api_bp.route("/get/rss/<param>")
async def get_rss_json(request,param):
    if param =='feed43':
        url = 'https://node2.feed43.com/8122477758625724.xml'
        feed = parse(url)
        articles = feed['entries']
        data = []
        for li in articles:
            data.append({
                'title':li['title_detail']['value'],
                'link':li['link'],
            })
        return json(data)
    else:
        return json({
            'info':'Please access ：http://127.0.0.1:8889/v1/get/rss/feed43'
        })
    return await template('index.html')

# post的请求参数
# @api_bp.route('/post/rss',methods=['POST'])
# async def post_rss_json(request,**kwargs): #
#     body_params = request.body
#     post_data = json_load(str(body_params,encoding='utf-8'))
#     name = post_data.get('name')
#     if name == 'feed43':
#         url = 'https://node2.feed43.com/8122477758625724.xml'
#         feed = parse(url)
#         articles = feed['entries']
#         data = []
#         for article in articles:
#             data.append({"title": article["title_detail"]["value"], "link": article["link"]})
#         return json(data)
#     else:
#         return json({'info': 'params error '})
#
@api_bp.route('/post/rss',methods=['POST'])
@auth_params('name')    # 先验证该参数是否存在
async def post_rss_json(request,**kwargs): #
    body_params = request.body
    post_data = json_load(str(body_params,encoding='utf-8'))
    name = post_data.get('name')
    if name == 'feed43':
        url = 'https://node2.feed43.com/8122477758625724.xml'
        feed = parse(url)
        articles = feed['entries']
        data = []
        for article in articles:
            data.append({"title": article["title_detail"]["value"], "link": article["link"]})
        return json(data)
    else:
        return json({'info': 'params error:1 '})
