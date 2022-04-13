import requests
import json
import urllib3
from lxml import etree
from bs4 import BeautifulSoup

url='https://searchtest.aminer.cn/aminer-operation/web/conf/getWebPublications'
# 请求头
headers = {
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'
}
# 请求体
data = {"fields":["id","year","title","title_zh","abstract",
                  "abstract_zh","authors.id","authors.name","authors.name_zh",
                  "keywords","n_citation","lang","pdf","ppt","url","resoureces"],
        "confId":"5fbf0f3692c7f9be218c86a6",
        "offset":0,"size":50,"sort":"view_num"}
# 返回结果处理
def get_request(url):
    urllib3.disable_warnings()
    try:
        IEEE_response = requests.post(url=url,data=json.dumps(data),headers=headers, verify=False)
        print("FINISH----:" + str(data['offset']))
    except:
        print("error----:"+str(data['offset']))
        return None
    response_text = IEEE_response.text
    res = json.loads(response_text)


    return res['data']['records']

offset = 0
pss = []
while True:
    ps = get_request(url)
    if ps is not None:
        pss += ps
        data['offset'] += 50
    if data["offset"]>1650:
        break

lns = []
for li in pss:
    try:
        tittle = li['publication']['title'].replace("\n","").replace("  "," ")
        href = li['publication']['url'][0]
        lns.append(f"{tittle}\t{href}\n")
    except:
        print(f'{tittle} err')
        continue

# 写入
emnlp_file = '../data/file_aaai21.txt'
with open (f'./{emnlp_file}','a',encoding='utf-8')as f:
    f.writelines(lns)
