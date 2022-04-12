# -*- coding: UTF-8 -*-
import argparse
import os

from xmly2 import utils

'''
文件目录结构示例
xmly
    Mjts
        origin
            __0001.m4a
        split
            __0001
                vocals.wav
                accompaniment.wav
        text
            __0001.srt
        cutting
            __0001_0001.wav
'''
dirNameList = ["origin","split","text","cutting"]

parser = argparse.ArgumentParser()
parser.add_argument("--save_root", default="F:\\xmly", type=str)
parser.add_argument("--album_path", default="album.json", type=str)
parser.add_argument("--wav_list_path", default="F:\\xmly\\wav.list", type=str)

def main():
    args = parser.parse_args()
    list_name = utils.read_album_name_json(args.album_path)

    for name in list_name:  # each album
        tmp_dir1 = os.path.join(args.save_root, name)
        if not os.path.exists(tmp_dir1):
            os.makedirs(tmp_dir1)
        for d in dirNameList:  # each sub for album
            tmp_dir2 = os.path.join(tmp_dir1, d)
            if not os.path.exists(tmp_dir2):
                os.makedirs(tmp_dir2)
    if not os.path.exists(args.wav_list_path):
        with open(args.wav_list_path, "w") as fp:
            pass

if __name__ == '__main__':
   main()

