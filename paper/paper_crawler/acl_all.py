import requests
import json
from lxml import etree
import bs4
from bs4 import BeautifulSoup
import urllib3
urllib3.disable_warnings()

url='https://aclanthology.org/events/acl-2021/'

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
    path = 'acl_all.html'
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

            lns_md.append(f'|{title}|acl21||{href}|\n')
            lns_smi.append(f'{title}\t{href}\n')
        except:
            pass

    return lns_md,lns_smi

lns_md,lns_smi = get_request(url)
# 写入
file_md = '../data/file_acl21_all_md.txt'
file_smi = '../data/file_acl21_all_smi.txt'

with open (f'./{file_md}','w',encoding='utf-8')as f:
    f.writelines(lns_md)
with open (f'./{file_smi}','w',encoding='utf-8')as f:
    f.writelines(lns_smi)
