# -*- coding: UTF-8 -*-
import argparse
import os
import ctr_autosub as ctr_autosub
# 需在 sutosub目录下执行

# 计算该文件所有音频时??

langCode = "zh"

def gene_subtitle(file_dir):
    count = 0
    for dirpath, dirnames, filenames in os.walk(file_dir):
        for i in filenames:
            sourceFile = os.path.join(file_dir,i)
            outputFileSRT = os.path.join(file_dir,"text",i.split(".")[0]+".srt")

            fOutput = ctr_autosub.Ctr_Autosub.generate_subtitles(source_path = sourceFile,
                                                                 output = outputFileSRT,
                                                                 src_language = langCode,
                                                                 listener_progress = None)
            print("gene subtitle finished:%s\n"%outputFileSRT)
        break

parser = argparse.ArgumentParser()
parser.add_argument("--save_root", default="D:\\temp_file", type=str)

if __name__ == '__main__':


    sourceFile = r"E:\test.wav"
    outputFileSRT = os.path.join( r"E:\test.srt")

    fOutput = ctr_autosub.Ctr_Autosub.generate_subtitles(source_path=sourceFile,
                                                         output=outputFileSRT,
                                                         src_language="th",
                                                         listener_progress=None)
    print("gene subtitle finished:%s\n" % outputFileSRT)

