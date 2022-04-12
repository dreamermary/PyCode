import os
def file_name(file_dir):
    sum = 0
    for dirpath, dirnames, filenames in os.walk(file_dir):
        for i in filenames:
            des_idx = str("%04d"%(int(i.split("_")[1].split(".")[0])))
            des_path = i.split("_")[0]+"_"+des_idx+".wav"
            os.rename(file_dir+'\\'+i, file_dir+'\\'+des_path)


def rename():
    file_name("D:\\temp_file\\巴黎圣母院\\cutting")

import re
if __name__ == '__main__':
    # rename()
    i = "《摸金天师》第001章_百辟刀.m4a"
    chapter = re.findall(r"\d+", i)
    print(int("0001"))