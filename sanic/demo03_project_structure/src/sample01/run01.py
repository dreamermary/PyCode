# -*- coding: utf-8 -*-
# @Author  :   clumba
# @File    :   run01.py
# @Time    :   2022/6/15 9:23

from sanic import Sanic
from sanic.response import json,html
from feedparser import parse
from jinja2 import Template

template = Template(
    """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>rss阅读</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
    </head>
    <body>
    <article class="markdown-body">
        {% for article in articles %}
        <b><a href="{{article.link}}">{{article.title}}</a></b><br/>
        <i>{{article.published}}</i><br/>
        <hr/>
        {% endfor %}
    </article>
    </body>
    </html>
    """
)

app = Sanic(name="app")

@app.route('/')
async def index(request):
    url = 'https://feed43.com/8122477758625724.xml'
    feed = parse(url) # 得到一个对象
    articles = feed['entries']
    data = []
    for article in articles:
        data.append({'title':article['title_detail']['value'],
                     'link':article['link']})
    return json(data)

@app.route('/html')
async def index(request):
    url = 'https://feed43.com/8122477758625724.xml'
    feed = parse(url) # 得到一个对象
    articles = feed['entries']
    data = []
    for article in articles:
        data.append({'title':article['title_detail']['value'],
                     'link':article['link']})

    html_content = template.render(articles=data)
    return html(html_content)

if __name__ == "__main__":
    app.run(host='127.0.0.1',port=8889)



