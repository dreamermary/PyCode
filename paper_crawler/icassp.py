import requests
import os
import json
import argparse
import urllib3

icassp_data = {
  "isnumber": 9413350,
  "pageNumber": 1,
  "punumber": "9413349",
  "rowsPerPage":100,
}
icassp_url = "https://ieeexplore.ieee.org/rest/search/pub/9413349/issue/9413350/toc"
icassp_file = 'file_icassp21.txt'

headers = {
    'Accept': 'application/json,text/plain,*/*',
    'Accept-Encoding': 'gzip,deflate,br',
    'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Content-Length': '56',
    'Content-Type': 'application/json',
    'Referer': f'https://ieeexplore.ieee.org/xpl/conhome/{icassp_data["punumber"]}/proceeding?isnumber={icassp_data["isnumber"]}&pageNumber={icassp_data["pageNumber"]}',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'

}

def get_response(url,data):
    urllib3.disable_warnings()
    try:
        response = requests.post(url=url, headers=headers,data=json.dumps(data),verify=False)
    except :
        print('-----错误url---'+data['pageNumber']+":"+url)

    try:
        response = json.loads(response.text)['records']
    except :
        print('-----错误json---'+data['pageNumber'])
        return None
    return response


def write_items(papers):
    lns  = []
    for p in papers:
        if p.__contains__('authors'):
            tittle = p['articleTitle']
            num = p['articleNumber']
            lns.append(f"{tittle}\t{num}\n")

    # 写入
    with open (f'./{icassp_file}','a')as f:
        f.writelines(lns)

page = 0
papers = []
while True:
    page += 1
    icassp_data['pageNumber'] = page
    res = get_response(icassp_url,icassp_data)
    if res is not None:
        print(f"{str(page)}：: finished")
        write_items(res)
    else:
        break


