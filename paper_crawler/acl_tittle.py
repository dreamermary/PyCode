import requests
import json
from lxml import etree
import bs4
from bs4 import BeautifulSoup

url='https://aclanthology.org/events/acl-2021/'

# 请求头
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip,deflate,br',
    'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'
}
# 请求体

# 返回结果处理
def get_request(url):
    IEEE_response = requests.get(url=url,headers=headers, verify=False)
    response_text = IEEE_response.text

    soup = BeautifulSoup(IEEE_response.content,'html.parser')
    ps = soup.find_all('section',class_="page__content")[0]

    res = []
    for i in ps.contents:
        if len(i)==4 :
            res.append(i)

    return res

ps = get_request(url)

pps = []
for p in ps:
    tittle = p.contents[0].string
    href = ""

    pps.append(f"{tittle}\n")

# 写入
acl_file = '../file_acl21.txt'
with open (f'./{acl_file}','a')as f:
    f.writelines(pps)
