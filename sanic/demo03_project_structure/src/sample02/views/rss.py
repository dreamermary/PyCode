# -*- coding: utf-8 -*-
# @Author  :   clumba
# @File    :   rss_html.py.py
# @Time    :   2022/6/15 10:50
import sys
from sanic import Sanic
from sanic.response import json, text, html
from feedparser import parse
from jinja2 import Environment, PackageLoader, select_autoescape


app = Sanic(name='app')

'''
# jinja2 config
异步方式引入jinja2
'''
enable_async = sys.version_info >= (3,6) # python 版本
env = Environment(
    loader=PackageLoader('views.rss', '../templates'), ## 这个路径怎么回事??
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


@app.route("/")
async def index(request):
    url = "https://node2.feed43.com/8122477758625724.xml"
    feed = parse(url)
    articles = feed['entries']
    data = []
    for article in articles:
        data.append({"title": article["title_detail"]["value"], "link": article["link"]})
    return json(data)

@app.route('/html')
async def rss_html(request):
    url = "https://node2.feed43.com/8122477758625724.xml"
    feed = parse(url)
    articles = feed['entries']
    data = []
    for article in articles:
        data.append(
            {"title": article["title_detail"]["value"], "link": article["link"], "published": article["published"]})
    return await template('rss.html', articles=articles)
    # await...