# -*- coding: utf-8 -*-
# @Author  :   clumba
# @File    :   demo01.py
# @Time    :   2022/6/14 10:01

import random
import aiohttp
from sanic import Sanic
from sanic.response import html,json,redirect
from sanic.exceptions import NotFound

size = 10
app = Sanic(name="app")

async def get_news(size =10 ):

    readhub_api = "https://api.readhub.me/topic"
    headers = {'content-type': 'application/json'}
    params = {'pageSize': size}

    all_news = []
    # 请求对象
    try:
        async with aiohttp.ClientSession() as client:
            # 发起请求
            async with client.get(readhub_api,params=params,headers=headers) as response:
                assert response.status == 200
                result = await response.json()

                for value in result.get('data',[]):
                    each_data = {}
                    each_data['title'] = value.get('title')
                    each_data['summary'] = value.get('summary')
                    each_data['news_info'] = value.get('newsArray')
                    each_data['updated_at'] = value.get('updatesAt')
                    all_news.append(each_data)

            return all_news

    except Exception as e:
        return all_news

@app.route('/<page:int>')
@app.route('/')
async def index(request,page=1):
    html_temp = \
        """
            <div>
                <p><a href="{href}">{title}</a></p>
                <p>{summary}</p>
                <p>{updated_at}</p>
            </div>
        """  # 单条的模板
    html_list = []  # 总的条

    all_news = await get_news(page*10) # 获取这么多页的数据,一页10条
    for li in all_news:
        html_list.append(html_temp.format(
            href=li.get("news_info"),
            title=li.get('title'),
            summary=li.get('summary'),
            updated_at=li.get('updated_at'),
        ))
    return html("<hr>".join(html_list))


# 加入请求参数，{nums,1},新闻数量
@app.route('/json')
async def index_json(request):
    nums = int(request.args.get('nums',1)[0])    # url中的参数
    all_news = await get_news() # list

    try:
        return json(random.sample(all_news,nums))
    except ValueError:
        return json(all_news)

# 注意路由 app.exception
@app.exception(NotFound)
def ignore_404s(request, exception):
    return redirect('/') # 重定向到新url

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8889)