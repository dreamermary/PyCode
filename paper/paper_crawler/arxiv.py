# -*- coding: utf-8 -*-
# @Author  :   clumba
# @File    :   arxiv.py.py
# @Time    :   2022/4/12 12:43
import requests
from bs4 import BeautifulSoup

keyword = 'aaai 2022'
offset=0
headers={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'
}
lis = []
for i in range(6):
    url = f'https://arxiv.org/search/?query={keyword}&searchtype=all&abstracts=show&order=-announced_date_first&size=100&start={offset}'
    response = requests.get(url)
    soup = BeautifulSoup(response.content,'html.parser')
    lis += soup.find_all("li", class_='arxiv-result')
    offset = (i+1)*100

lns = []
lns2 = []
for li in lis:
    href = li.contents[1].contents[1].contents[0].attrs['href']
    title = li.contents[3].contents[0].strip()
    lns.append(f'|{title}|aaai22||{href}|\n')
    lns2.append(f'{title}\t{href}\n')

icassp22_file = '../file_aaai22.txt'
icassp22_file2 = '../file_aaai22.txt'
with open (f'./{icassp22_file}','w')as f:
    f.writelines(lns)
with open (f'./{icassp22_file2}','w')as f:
    f.writelines(lns2)
