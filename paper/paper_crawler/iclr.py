import requests
import json
from lxml import etree
from bs4 import BeautifulSoup
import urllib

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
base_url = 'https://api.openreview.net/notes?'
paper_url =''
def get_request(base_url):
    offset = 0

    tps_smi,tps_md = [],[]

    bld_ps,dec_ps = {},[]
    while True:
        bld_params = f'invitation=ICLR.cc/2021/Conference/-/Blind_Submission&details=replyCount,invitation,original&limit=1000&offset={offset}'
        dec_params = f'invitation=ICLR.cc/2021/Conference/Paper.*/-/Decision&limit=1000&offset={offset}'
        bld_response = requests.get(url=base_url+bld_params,headers=headers, verify=False).json()
        dec_response = requests.get(url=base_url+dec_params,headers=headers, verify=False).json()


        for i in bld_response['notes']:
            bld_ps[i['forum']] = [i['content']['title'],f'https://openreview.net/forum?id={i["forum"]}']

        for i in dec_response['notes']:
            if 'Accept' in i['content']['decision']:
                dec_ps.append(i['forum'])

        count = max(bld_response["count"],dec_response['count'])
        offset += 1000
        if offset > count:
            break

    return bld_ps,dec_ps

bld_ps,dec_ps = get_request(base_url)

tps_md,tps_smi=[],[]
bld_ps.keys()
for p in dec_ps:
    try:
        lis = bld_ps[p]

        tps_smi.append(f'{lis[0]}\t{lis[1]}\n')
        tps_md.append(f'|{lis[0]}|iclr21||{lis[1]}|\n')
    except:
        print(p)
11
# 写入
file_md = '../data/file_iclr21_md.txt'
file_smi = '../data/file_iclr21_smi.txt'
with open (f'./{file_md}','w',encoding='utf-8')as f:
    f.writelines(tps_md)
with open (f'./{file_smi}','w',encoding='utf-8')as f:
    f.writelines(tps_smi)
