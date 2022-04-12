import argparse

import librosa
import os
from xmly2 import utils


# 计算该文件所有音频时长
def caculate_length(file_dir):
    sum = 0
    for dirpath, dirnames, filenames in os.walk(file_dir):
        for i in filenames:
            path = os.path.join(file_dir,i)
            duration = librosa.get_duration(filename=path)
            sum += duration
    return sum



parser = argparse.ArgumentParser()
parser.add_argument("--save_root", default="F:\\xmly", type=str)
parser.add_argument("--album_path", default="album.json", type=str)

if __name__ == '__main__':

    args = parser.parse_args()

    sum = 0
    dir = args.save_root
    dirs = utils.read_album_name_json(args.album_path) ## ["album1","album2",...]
    for d in dirs:
        li = caculate_length(os.path.join(dir,d,"origin"))
        sum += li
    print(sum/60)