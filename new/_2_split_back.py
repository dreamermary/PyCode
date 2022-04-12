# -*- coding: UTF-8 -*-
import argparse
import os
from concurrent.futures.thread import ThreadPoolExecutor

from xmly2 import utils


def spleeter(cmd):
    os.system(cmd)

def split_back(file_dir): # xmly/hdlwl
    thread_list = []
    for dirpath, dirnames, filenames in os.walk(os.path.join(file_dir,"origin")):
        for i in filenames:
            path = os.path.join(file_dir,i)
            cmd1 = "cd "+args.spleeter_path
            cmd2 = "spleeter separate -p spleeter:2stems -o "+os.path.join(file_dir,"split")+"  "+path+" -d 3600"
            ## -o output ; -d 最大长度/s,超过则舍去; -i(废弃) input
            # os.system(cmd1+" && "+cmd2)
            trd = pool.submit(spleeter,cmd1+" && "+cmd2)
            thread_list.append(trd)
            print("Thread added: %s"  % path)
    print([i.result() for i in thread_list])



parser = argparse.ArgumentParser()
parser.add_argument("--save_root", default="F:\\xmly", type=str)
parser.add_argument("--album_path", default="album.json", type=str)
parser.add_argument("--spleeter_path", default="E:\\softdata\\pycharm\\venv\\crawler\\Lib\\site-packages\\spleeter", type=str)
args = parser.parse_args()
def main():
    pool = ThreadPoolExecutor(max_workers=10)
    dir = args.save_root
    dirs = utils.read_album_name_json(args.album_path)  ## ["album1","album2",...]
    for d in dirs:
        li = split_back(os.path.join(dir, d))
    pool.shutdown()
if __name__ == '__main__':

    main()



# ''' test'''
# if __name__ == '__main__':
#     args = parser.parse_args()
#     ipath = "D:\\temp_file\\鬼吹灯\\鬼吹灯之云南虫谷26.m4a"
#     opath = "D:\\temp_file\\鬼吹灯\\output"
#
#     cmd1 = "cd " + args.spleeter_path
#     cmd2 = "spleeter separate -p spleeter:2stems -o " + opath + "  " + ipath + " -d 3600"
#     ## -o output ; -d 最大长度/s,超过则舍去; -i(废弃) input
#     os.system(cmd1 + " && " + cmd2)
#     print("ok")
