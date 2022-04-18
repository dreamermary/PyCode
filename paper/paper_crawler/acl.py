import requests
import json
from lxml import etree
import bs4
from bs4 import BeautifulSoup
import urllib3
urllib3.disable_warnings()

url='https://aclanthology.org/events/naacl-2021/'

# 请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'
}
# 请求体

# 返回结果处理
def get_request(url):
    # IEEE_response = requests.get(url=url,headers=headers, verify=False)
    # response_text = IEEE_response.text

    # 本地读取
    path = '../data/naacl21.html'
    # soup = BeautifulSoup(IEEE_response,'html.parser')
    soup = BeautifulSoup(open(path,encoding='utf-8'),'html.parser')
    ps = soup.find_all('p',class_="d-sm-flex align-items-stretch")


    lns_md,lns_smi = [],[]
    # 解析
    for p in ps:
        try:
            # href
            href = p.contents[1].contents[0].contents[0].attrs['href']
            # title
            title = p.contents[1].contents[0].text

            lns_md.append(f'|{title}|{conf}{ysim}||{href}|\n')
            lns_smi.append(f'{title}\t{href}\n')
        except:
            pass

    return lns_md,lns_smi

year = '2021'
ysim = '21'
conf = 'naacl'
lns_md,lns_smi = get_request(url)
# 写入


file_md = f'../data/file_{conf}{ysim}_md.txt'
file_smi = f'../data/file_{conf}{ysim}_smi.txt'

with open (f'./{file_md}','w',encoding='utf-8')as f:
    f.writelines(lns_md)
with open (f'./{file_smi}','w',encoding='utf-8')as f:
    f.writelines(lns_smi)
