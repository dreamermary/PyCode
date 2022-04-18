# -*- coding: utf-8 -*-
# @Author  :   clumba
# @File    :   16k.py.py
# @Time    :   2022/4/13 17:59
import requests
import json
import urllib3
import datetime
import schedule
import time
urllib3.disable_warnings()

headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6Im1obCIsInByaXZpbGVnZXMiOlsiSk9CIl0sImlhdCI6MTY0OTc3MjEzNSwiZXhwIjoxNjUwMzc2OTM1fQ.drMiDTFhz7maYeoj6qnHJXqtWd1kw4fKItk6fbx4dhI",
    "Connection": "keep-alive",
    "Content-Type": "text/yaml",
    "Cookie": "user=mhl; token=eyJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6Im1obCIsInByaXZpbGVnZXMiOlsiSk9CIl0sImlhdCI6MTY0OTc3MjEzNSwiZXhwIjoxNjUwMzc2OTM1fQ.drMiDTFhz7maYeoj6qnHJXqtWd1kw4fKItk6fbx4dhI; admin=false; jobSubmitMode=true",
    "Host": "222.197.219.19",
    "Origin": "http://222.197.219.19",
    "Referer": "http://222.197.219.19/job-submit",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"
}
url = "http://222.197.219.19/rest-server/api/v2/jobs"

def apply_card(freecard):
    data = open('params.yaml',encoding='utf-8').read().replace('freecard',freecard).encode('utf-8')
    response = requests.post(url=url, data=data, headers=headers, verify=False)
    res_json = response.json()
    if res_json['code'] == 'OperateFailed':
        # 申请失败
        print(str(datetime.datetime.now())+f"：{freecard} 空闲申请失败")
    else:
        #申请成功
        print(str(datetime.datetime.now()) + f"：{freecard} 空闲申请成功")


query_url = 'http://222.197.219.19/java-rest-server/api/user/mhl/canUseVirtualGroups?withInfo=true'
query_headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6Im1obCIsInByaXZpbGVnZXMiOlsiSk9CIl0sImlhdCI6MTY0OTc3MjEzNSwiZXhwIjoxNjUwMzc2OTM1fQ.drMiDTFhz7maYeoj6qnHJXqtWd1kw4fKItk6fbx4dhI",
    "Connection": "keep-alive",
    "Cookie": "user=mhl; token=eyJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6Im1obCIsInByaXZpbGVnZXMiOlsiSk9CIl0sImlhdCI6MTY0OTc3MjEzNSwiZXhwIjoxNjUwMzc2OTM1fQ.drMiDTFhz7maYeoj6qnHJXqtWd1kw4fKItk6fbx4dhI; admin=false; jobSubmitMode=true",
    "Host": "222.197.219.19",
    "Origin": "http://222.197.219.19",
    "Referer": "http://222.197.219.19/job-submit",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"
}
def query_card():
    freecard = 0
    response = requests.get(query_url,headers=query_headers, verify=False)
    res_json = response.json()
    for res in res_json:
        if res['activeJobs']==0:
            return res['name']
    # 查询
    print(str(datetime.datetime.now()) + f"：无卡")
    return None

def job():
    freecard = query_card()
    if freecard is not None:
        apply_card(freecard)

query_card()
# schedule.every(30).minutes.do(job)
#
# while True:
#     schedule.run_pending()
#     time.sleep(1)
