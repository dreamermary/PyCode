# -*- coding: utf-8 -*-
# @Time  : 2021/4/1 10:26
# @Author : lovemefan
# @File : sign.py
import argparse
import sys
import time
import json
import requests
import schedule as schedule
import os
import random

class WozaixiaoyuanSign(object):
    def __init__(self, username, password, sc_key=None):
        self.username = username
        self.password = password
        self.sc_key = sc_key
        self.status_code = -10
        self.jwsession = None
        self.message = ""
        self.headers = {
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat",
            "Content-Type": "application/json;charset=UTF-8",
            "Content-Length": "2",
            "Host": "gw.wozaixiaoyuan.com",
            "Accept-Language": "en-us,en",
            "Accept": "application/json, text/plain, */*"
        }
        self.body = "{}"

    def login(self):
        url = f'https://gw.wozaixiaoyuan.com/basicinfo/mobile/login/username?username={self.username}&password={self.password}'
        print(url)
        # 登录
        if not self.jwsession or self.status_code == -10:
            response = requests.post(url=url, data=self.body, headers=self.headers)
            res = json.loads(response.text)
            self.status_code = res["code"]
            if res["code"] == 0:
                print("使用账号信息登录成功")
                self.set_jwsession(response.headers['JWSESSION'])
                return True
            else:
                print(res)      
                print("登录失败，请检查账号信息")
                sys.exit()

        return True

    def get_result(self, response):
        res = response['code']
        if res == 0:
            return f"✅ 打卡成功, {self.message}"
        elif res == 1:
            return f"❌ 打卡失败，{self.message}"
        elif res == -10:
            return "❌ 打卡失败，jwsession 无效"
        elif res == 5:
            return "❌ 打卡失败，登录错误，请检查账号信息"
        elif res == 101:
            return "❌ 登录失败，请检查账号和密码"
        else:
            return f"❌ 打卡失败，{self.message}"

    def set_jwsession(self, jwsession):
        # 如果找不到cache,新建cache储存目录与文件
        if not os.path.exists('.cache'):
            print("正在创建cache储存目录与文件...")
            os.mkdir('.cache')
            data = {"jwsession": jwsession}
        elif not os.path.exists(f'.cache/{self.username}_cache.json'):
            print("正在创建cache文件...")
            data = {"jwsession": jwsession}
        # 如果找到cache,读取cache并更新jwsession
        else:
            print("找到cache文件，正在更新cache中的jwsession...")
            jwsession = self.get_jwsession()
            data = {"jwsession": jwsession}

        with open(f'.cache/{self.username}_cache.json', 'w') as f:
            json.dump(data, f)
        self.jwsession = data['jwsession']

    def get_jwsession(self):
        if not self.jwsession:  # 读取cache中的配置文件
            with open(f'.cache/{self.username}_cache.json', 'r') as f:
                data = json.load(f)
                self.jwsession = data['jwsession']
        return self.jwsession

    def daily_sign(self, seq: int, sign_type=0):
        """日检日报打卡
        :param sc_key: Server酱的sc_key
        :param seq: 1为晨检，2为午检，3为晚检
        :param sign_type: 类型，0表示日检日报，1表示健康打卡
        """

        if sign_type == 0:
            url = 'https://student.wozaixiaoyuan.com/heat/save.json'
        else:
            url = 'https://student.wozaixiaoyuan.com/health/save.json'
        data = {
            "answers": "[\"0\"]",
            "seq": seq,
            "temperature": "36.4",
            "latitude": "24.852266",
            "longitude": "102.857704",
            "country": "中国",
            "city": "昆明市",
            "district": "呈贡区",
            "province": "云南省",
            "township": "吴家营街道",
            "street": "景明南路",
            "myArea": "呈贡校区",
            "areacode": "530114"
        }
        if self.login():
            self.headers['Host'] = "student.wozaixiaoyuan.com"
            self.headers['Content-Type'] = "application/x-www-form-urlencoded"
            self.headers['JWSESSION'] = self.get_jwsession()
            response = requests.post(url, data=data, headers=self.headers)
            response = json.loads(response.text)
         
            self.status_code = response["code"]
            self.message = response.get("message", "")

            # 发送微信
            # 微信推送http://sc.ftqq.com
            if self.sc_key and response['code'] != 0 and response['code'] != 1:
                url = f"https://sctapi.ftqq.com/{self.sc_key}.send?text=每日打卡签到失败&desp={response['message']}"
                print(f"url: {url}")
                res = requests.get(url)
                print(res)

            if sign_type == 1:
                print(f"【{time.asctime()}】 每日健康打卡")
            elif seq == 1:
                print(f"【{time.asctime()}】 晨检打卡")
            elif seq == 2:
                print(f"【{time.asctime()}】 午检打卡")
            else:
                print(f"【{time.asctime()}】 晚检打卡")

            print(self.get_result(response).encode('GBK','ignore').decode('GBK'))
        else:
            pass

    def run(self):

        self.daily_sign(2,0)
        # # 健康打卡
        # schedule.every().day.at(f"10:0{str(random.randint(1,9))}").do(self.daily_sign, 1, 1)
        # # 日检
        # schedule.every().day.at(f"07:3{str(random.randint(1,9))}").do(self.daily_sign, 1, 0)
        # # 午检
        # schedule.every().day.at(f"12:0{str(random.randint(1,9))}").do(self.daily_sign, 2, 0)
        # # 晚检
        # schedule.every().day.at(f"22:0{str(random.randint(1,9))}").do(self.daily_sign, 3, 0)
        # # 测试
        # schedule.run_all()
        # while True:
        #     schedule.run_pending()
        #     time.sleep(5)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--username', help='input you username', default="18834355830")
    parser.add_argument('-p', '--password', help='input you password', default="654321")
    args = parser.parse_args()

    sign = WozaixiaoyuanSign(args.username, args.password)
    sign.run()

