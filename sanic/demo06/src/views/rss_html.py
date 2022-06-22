# -*- coding: utf-8 -*-
# @Author  :   clumba
# @File    :   rss_html.py.py
# @Time    :   2022/6/15 10:50
import sys
from sanic.response import json, text, html
from feedparser import parse
from jinja2 import Environment, PackageLoader, select_autoescape
from sanic import Blueprint
import os

from src.config import CONFIG


'''
BluePrint,
    路由，及其静态资源
'''
html_bp = Blueprint('rss_html',url_prefix='html') # name,prefix
html_bp.static(
    '/statics/rss_html',
    os.path.join(CONFIG.BASE_DIR,'statics/rss_html')
) # 静态目录,静态目录

'''
# jinja2 config
    异步方式引入jinja2
    路由文件，html路径,
'''
enable_async = sys.version_info >= (3,6) # python 版本
env = Environment(
    loader=PackageLoader('views.rss_html', '../templates/rss_html'), ## 这个路径怎么回事??
    autoescape=select_autoescape(['html', 'xml', 'tpl']),
    enable_async=enable_async,
)

async def template(tpl, **kwargs):# tmp.html,data
    template = env.get_template(tpl)
    rendered_template = await template.render_async(**kwargs)
    return html(rendered_template)
'''
Environment().get_template().render_async()
'''

@html_bp.route("/")
async def index(request):
    return await template('index.html')

# 真实 url = (url_prefix+route) = /html/index
@html_bp.route('/index')
async def rss_html(request):
    url = "https://node2.feed43.com/8122477758625724.xml"
    feed = parse(url)
    articles = feed['entries']
    data = []
    for article in articles:
        data.append(
            {"title": article["title_detail"]["value"],
             "link": article["link"],
             "published": article["published"]})
    return json(data)
    # await...