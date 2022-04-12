# -*- coding: UTF-8 -*-
import argparse
import os
import re

def split_back(file_dir): # xmly/hdlwl
    for dirpath, dirnames, filenames in os.walk(file_dir):
        for i in dirnames:
            path = os.path.join(file_dir,i, "accompaniment.wav")
            try:
                os.remove(path)
                print("del success:%s"%path)
            except:
                print("del faile:%s" % path)



parser = argparse.ArgumentParser()
parser.add_argument("--save_root", default="E:\\file\\xmla_audio", type=str)
parser.add_argument("--spleeter_path", default="E:\\softdata\\pycharm\\venv\\crawler\\Lib\\site-packages\\spleeter", type=str)

if __name__ == '__main__':
    # os.remove("0.txt")
    args = parser.parse_args()
    dir = args.save_root
    for d in ["摸金天师"]:
        li = split_back(os.path.join(dir, d,"output"))

# ''' test'''
# if __name__ == '__main__':
#     args = parser.parse_args()
#     ipath = "E:\\file\\xmla_audio\\摸金天师\\《摸金天师》第1046章_疯王.m4a"
#     opath = "E:\\file\\xmla_audio\\摸金天师\\output"
#
#     cmd1 = "cd " + args.spleeter_path
#     cmd2 = "spleeter separate -p spleeter:2stems -o " + opath + "  " + ipath + " -d 3600"
#     ## -o output ; -d 最大长度/s,超过则舍去; -i(废弃) input
#     os.system(cmd1 + " && " + cmd2)
#     print("ok")
