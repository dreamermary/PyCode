# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import argparse
import os
from concurrent.futures.thread import ThreadPoolExecutor

import new.utils
import  ctr_autosub
# 需在 sutosub目录下执行

# 计算该文件所有音频时??

langCode = "zh"

def gene_subtitle(file_dir):
    count = 0
    for dirpath, dirnames, filenames in os.walk(os.path.join(file_dir,"origin")):
        for i in filenames:
            sourceFile = os.path.join(file_dir,i)
            outputFileSRT = os.path.join(file_dir,"text",i.split(".")[0]+".srt")

            fOutput = ctr_autosub.Ctr_Autosub.generate_subtitles(source_path = sourceFile,
                                             output = outputFileSRT,
                                             src_language = langCode,
                                             listener_progress = None)
            print("gene subtitle finished:%s\n"%outputFileSRT)


parser = argparse.ArgumentParser()
parser.add_argument("--save_root", default="F:\\xmly", type=str)
parser.add_argument("--album_path", default="album.json", type=str)

def main():
    pool = ThreadPoolExecutor(max_workers=10)
    thread_list = []
    args = parser.parse_args()

    dir = args.save_root
    dirs = utils.read_album_name_json(args.album_path)  # ['鬼吹灯', '巴黎圣母院']
    for name in dirs:

        # li = gene_subtitle(os.path.join(dir, name))

        path = os.path.join(dir, name)
        trd = pool.submit(gene_subtitle, path)
        thread_list.append(trd)
        print("Thread added: %s" % path)
        # download_and_save(os.path.join(args.save_root, album_name, "origin"), li[1], li[2])
    print([i.result() for i in thread_list])
    pool.shutdown()

def temp():

    sourceFile = os.path.join(r"E:\file\xmla_audio\test", "exmp.mp3")
    outputFileSRT = os.path.join(r"E:\file\xmla_audio\test", "exmp" + ".srt")

    fOutput = ctr_autosub.Ctr_Autosub.generate_subtitles(source_path=sourceFile,
                                                         output=outputFileSRT,
                                                         src_language=langCode,
                                                         listener_progress=None)
    print("gene subtitle finished:%s\n" % outputFileSRT)

if __name__ == '__main__':

    # main()
    temp()

