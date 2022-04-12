import requests
import json
from lxml import etree
from bs4 import BeautifulSoup

url='https://searchtest.aminer.cn/aminer-operation/web/conf/getWebPublications'
# 请求头
headers = {
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'
}
# 请求体
data = {"fields":["id","year","title","title_zh","abstract","abstract_zh",
                  "authors.id","authors.name","authors.name_zh","keywords",
                  "n_citation","lang","pdf","ppt","url","resoureces"],
        "confId":"613f4cae92c7f9be2110f43e","offset":0,"size":50,"sort":"view_num"}
# 返回结果处理
def get_request(url):
    IEEE_response = requests.post(url=url,data=json.dumps(data),headers=headers, verify=False)
    response_text = IEEE_response.text
    res = json.loads(response_text)


    return res['data']['records']

offset = 0
pss = []
while True:
    ps = get_request(url)
    pss += ps
    data['offset'] += 50

lns = []
for li in pss:
    tittle = li['publication']['tittle']
    href = li['publication']['url'][0]
    lns.append(f"{tittle}\t{href}\n")

# 写入
emnlp_file = '../file_emnlp21.txt'
with open (f'./{emnlp_file}','a')as f:
    f.writelines(lns)
