import requests
import os
import json
import argparse
import urllib3

urllib3.disable_warnings()
def gene_params(isnumber, punumber,pageNumber):
    icassp_data = {
        "isnumber": isnumber,
        "pageNumber": pageNumber,
        "punumber": punumber,
        "rowsPerPage":500,
    }

    headers = {
        'Accept': 'application/json,text/plain,*/*',
        'Accept-Encoding': 'gzip,deflate,br',
        'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Content-Length': '56',
        'Content-Type': 'application/json',
        # 'Referer': f'https://ieeexplore.ieee.org/xpl/conhome/{icassp_data["punumber"]}/proceeding?isnumber={isnumber}&pageNumber={icassp_data["pageNumber"]}',
        'Referer':f'https://ieeexplore.ieee.org/xpl/conhome/{punumber}/proceeding',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'
    }

    return icassp_data,headers

def get_response(url,data,headers):
    response = requests.post(url=url, headers=headers,data=json.dumps(data),verify=False)
    res = response.json()
    if (data['pageNumber']-1)*500 > res['totalRecords']:
        return None

    lns = []
    for li in res['records'] :
        title = li['articleTitle']
        href = 'https://ieeexplore.ieee.org/document/'+li['articleNumber']
        lns.append([title,href])

    return lns



def write_items(papers):
    lns_md,lns_sim  = [],[]
    for p in papers:
        tittle = p[0]
        href = p[1]
        lns_sim.append(f"{tittle}\t{href}\n")
        lns_md.append(f"|{tittle}|{conf}{_year}||{href}|\n")

    file_md = f'../data/file_{conf}{_year}_md.txt'
    file_smi = f'../data/file_{conf}{_year}_smi.txt'

    # 写入
    with open (f'./{file_md}','a',encoding='utf-8')as f:
        f.writelines(lns_md)
    with open (f'./{file_smi}','a',encoding='utf-8')as f:
        f.writelines(lns_sim)

# isnumber = 9413350
# punumber = '9413349'
# conf = 'icassp'
# year = '2021'
# _year = '21'
# icassp_url = f"https://ieeexplore.ieee.org/rest/search/pub/{punumber}/issue/{isnumber}/toc"
# icassp_file = f'file_{conf}{_year}.txt'

isnumber = 9052899
punumber = '9040208'
conf = 'icassp'
year = '2020'
_year = '20'
icassp_url = f"https://ieeexplore.ieee.org/rest/search/pub/{punumber}/issue/{isnumber}/toc"
icassp_file = f'file_{conf}{_year}.txt'

page = 0
papers = []

while True:
    print("page:")
    page += 1
    data,headers = gene_params(isnumber,punumber,pageNumber=page)
    lns = get_response(icassp_url,data,headers)

    if lns is None:break
    papers += lns

write_items(papers)


