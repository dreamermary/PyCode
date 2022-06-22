# -*- coding: utf-8 -*-
# @Author  :   clumba
# @File    :   run01.py
# @Time    :   2022/6/15 9:23

import sys
import os
from views.rss import app
from config.config import Config

# 添加环境变量？./sample02
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

app.static('./statics', os.path.join(Config.BASE_DIR, 'statics'))

if __name__ == "__main__":
    app.run(host='127.0.0.1',port=8889)



