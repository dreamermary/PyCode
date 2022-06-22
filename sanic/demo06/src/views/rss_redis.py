# -*- coding: utf-8 -*-
# @Author  :   clumba
# @File    :   rss_html.py.py
# @Time    :   2022/6/15 10:50
import sys
from sanic import Sanic,Blueprint
from sanic.response import json, text, html
from feedparser import parse
import asyncio
from aiocache import cached,RedisCache
from aiocache.serializers import PickleSerializer

'''
POST/GET:参数验证
'''
redis_bp = Blueprint('rss_redis',url_prefix='redis')

@cached(ttl=1000,cache=RedisCache,key='rss_json',
        serializer=PickleSerializer(),port=6379,namespace='main')
async def get_rss():
    print('第一次请求休眠3秒')
    await asyncio.sleep(3)
    url = "https://node2.feed43.com/8122477758625724.xml"
    feed = parse(url)
    articles = feed['entries']
    data = []
    for article in articles:
        data.append({"title": article["title_detail"]["value"], "link": article["link"]})
    return data
    pass

@redis_bp.route('/get/rss/<name>')
async def get_rss_json(request,name):
    if name == 'feed43':
        data = await get_rss()
        return json(data)
    else:
        return json({'info':'xxx'})
