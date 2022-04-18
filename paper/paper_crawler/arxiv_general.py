# -*- coding: utf-8 -*-
# @Author  :   clumba
# @File    :   arxiv.py.py
# @Time    :   2022/4/12 12:43
import requests
from bs4 import BeautifulSoup

headers={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'
}


def loop(conf,keywords):
    lis = []
    for keyword in keywords:
        offset = 0
        while True:
            url = f'https://arxiv.org/search/?query={keyword}&searchtype=all&abstracts=show&order=-announced_date_first&size=100&start={offset}'
            offset+=100
            response = requests.get(url)
            soup = BeautifulSoup(response.content,'html.parser')

            _ls = soup.find_all("li", class_='arxiv-result')
            lis += _ls

            if _ls is None or len(_ls)<100:
                break
    lns_md,lns_sim = [],[]
    for li in lis:
        href = li.contents[1].contents[1].contents[0].attrs['href']
        title = li.contents[3].contents[0].strip()
        lns_md.append(f'|{title}|{conf}||{href}|\n')
        lns_sim.append(f'{title}\t{href}\n')

    return lns_md,lns_sim



conf = 'emnlp'
year = '2022'
_year = '22'
keywords = [f'{conf} {year}',f'{conf}{year}',]
base_path = r'../data'
file_md = f'{base_path}/file_{conf}{_year}_md.txt'
file_sim = f'{base_path}/file_{conf}{_year}_smi.txt'

lns_md,lns_sim   = loop(conf+_year,keywords)


with open (f'./{file_sim}','w',encoding='utf-8')as f:
    f.writelines(lns_sim)
with open (f'./{file_md}','w',encoding='utf-8')as f:
    f.writelines(lns_md)
