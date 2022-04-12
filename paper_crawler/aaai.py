import requests
import json
from lxml import etree
from bs4 import BeautifulSoup

url_1='https://aaai.org/Library/AAAI/aaai21-issue14.php#27'
url_2='https://aaai.org/Library/AAAI/aaai21-issue14.php#28'
url_3='https://aaai.org/Library/AAAI/aaai21-issue14.php#29'
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
    ps = soup.find_all('p',class_="left")

    return ps

ps = []
for url in [url_1,url_2,url_3]:
    _ps = get_request(url)
    ps+= _ps

pps = []
for p in ps:
    href = p.contents[1].attrs['href']
    tittle = p.contents[1].string.strip().replace("\n","").replace("  ","")

    pps.append(f"{tittle}\t{href}\n")

# 写入
aaai_file = '../file_aaai21_nlp.txt'
with open (f'./{aaai_file}','a')as f:
    f.writelines(pps)
