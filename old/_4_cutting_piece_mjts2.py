import argparse
import os
from concurrent.futures.thread import ThreadPoolExecutor

import new.utils as utils


def add_wav_list(path,lines):
    with open(path,'a',encoding='utf-8')as f:
        f.writelines(lines)


# 读取一个字幕文件返回时间戳列表
def get_stamps(path):
    stamps_list = []
    subtitle_list = []
    try:
        with open(path,encoding="utf-8")as f:
            lines = f.readlines()
            for i in range(0,(len(lines)//4),1):
                li = lines[4*i+1]
                stamp = li.split(" --> ")
                start = stamp[0].rstrip()
                end = stamp[1].rstrip()
                stamps = [start.replace(',','.'),end.replace(',','.')]
                stamps_list.append(stamps)

                subtitle_list.append(lines[4*i+2].rstrip())
    except:
        pass
    #     stamps_list = []
    #     with open("D:\\temp_file\\鬼吹灯\\text\\error.log", "a",encoding="utf-8")as f:
    #         f.write(path+":"+"no this file\n")
    return stamps_list,subtitle_list

def cut(cmd_list):
    for i in cmd_list:
        os.system(i)



def cut_piece(file_dir):
    prefix = r"摸金天师\cutting\\"
    list_file = []
    for dirpath, dirnames, filenames in os.walk(os.path.join(file_dir,"cutting")):
        for filename in filenames:
            list_file.append(prefix+filename+"\n")
    add_wav_list(args.wav_list_path,list_file)
parser = argparse.ArgumentParser()
parser.add_argument("--save_root", default=r"F:\xmly", type=str)
parser.add_argument("--wav_list_path", default=r"F:\xmly\unlabel.mjts.wav.lst", type=str)

if __name__ == '__main__':
    args = parser.parse_args()

    dir = args.save_root
    for d in ["摸金天师"]:
        li = cut_piece(os.path.join(dir, d))
    print("------------ok------------")
