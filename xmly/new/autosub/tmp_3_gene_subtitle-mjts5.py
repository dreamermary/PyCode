# -*- coding: UTF-8 -*-
import argparse
import os
import ctr_autosub as ctr_autosub
import re
# 需在 sutosub目录下执行

# 计算该文件所有音频时??

langCode = "zh"

def gene_subtitle(file_dir):
    count = 0
    for dirpath, dirnames, filenames in os.walk(file_dir):
        for i in filenames:
            chapter = re.findall(r"\d+",i)
            if (len(chapter)>1 and (int(chapter[0])>=900 and int(chapter[0])<1000)) :
                sourceFile = os.path.join(file_dir,i)
                outputFileSRT = os.path.join(file_dir,"text",i.split(".")[0]+".srt")

                fOutput = ctr_autosub.Ctr_Autosub.generate_subtitles(source_path = sourceFile,
                                                                     output = outputFileSRT,
                                                                     src_language = langCode,
                                                                     listener_progress = None)
                print("gene subtitle finished:%s\n"%outputFileSRT)
        break

parser = argparse.ArgumentParser()
parser.add_argument("--save_root", default="E:\\file\\xmla_audio", type=str)

if __name__ == '__main__':

    args = parser.parse_args()

    dir = args.save_root
    for name in ["摸金天师"]:
        li = gene_subtitle(os.path.join(dir, name))
#
# if __name__ == '__main__':
#     sourceFile = os.path.join(r"D:\temp_file\月亮与六便士","月亮与六便士043.m4a")
#     outputFileSRT = os.path.join(r"D:\temp_file\月亮与六便士","月亮与六便士043.srt")
#
#     fOutput = ctr_autosub.Ctr_Autosub.generate_subtitles(source_path = sourceFile,
#                                      output = outputFileSRT,
#                                      src_language = langCode,
#                                      listener_progress = None)
#     print("gene subtitle finished:%s\n"%outputFileSRT)
#
#     sourceFile = os.path.join(r"D:\temp_file\月亮与六便士", "月亮与六便士045.m4a")
#     outputFileSRT = os.path.join(r"D:\temp_file\月亮与六便士", "月亮与六便士045.srt")
#
#     fOutput = ctr_autosub.Ctr_Autosub.generate_subtitles(source_path=sourceFile,
#                                                          output=outputFileSRT,
#                                                          src_language=langCode,
#                                                          listener_progress=None)
#     print("gene subtitle finished:%s\n" % outputFileSRT)