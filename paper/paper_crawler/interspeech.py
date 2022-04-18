import requests
import json
from lxml import etree
from bs4 import BeautifulSoup

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

    soup = BeautifulSoup(IEEE_response.content,'html.parser')
    ps = soup.find_all('div',class_="w3-container",attrs={"style":"margin-top:40px"})

    tps_smi,tps_md = [],[]
    for p in ps:
        topic = p.find('h4').text
        ass = p.find_all("a")

        for a in ass:
            href = base_url+a.attrs['href']
            title = a.text.strip().split('\n')[0]
            tps_smi.append(f"{title}\t{href}\t{topic}\n")
            tps_md.append(f"|{title}|{href}|{conf}{_year}|{topic}|\n")
    return tps_smi,tps_md

conf = 'interspeech'
year = '2021'
_year = '21'
url=f'https://www.isca-speech.org/archive/{conf}_{year}/index.html'
base_url = f'https://www.isca-speech.org/archive/{conf}_{year}/'

tps_smi,tps_md = get_request(url)

# 写入
file_md = f'../data/file_{conf}{_year}_md.txt'
file_smi = f'../data/file_{conf}{_year}_smi.txt'
with open (f'./{file_md}','w',encoding='utf-8')as f:
    f.writelines(tps_md)
with open (f'./{file_smi}','w',encoding='utf-8')as f:
    f.writelines(tps_smi)
