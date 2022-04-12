import os

# 计算该文件所有音频时??
def file_name(file_dir):
    for dirpath, dirnames, filenames in os.walk(file_dir):
        for i in filenames:
            path = file_dir+'\\'+i
            chapter = int(re.findall(r"\d+",path)[0])
            if chapter>=519 and chapter<= 999:
                cmd1 = "cd E:\\softdata\\pycharm\\venv\\crawler\\Lib\\site-packages\\spleeter "
                cmd2 = "spleeter separate -p spleeter:2stems -o "+file_dir+"\\output"+"  "+path+" -d 3600"
                os.system(cmd1+" && "+cmd2)
                print(path)

            # print(cmd1)
            # print(cmd2)
            # os.rename(path, path.replace(" ","_"))
            # print(path.replaceAll(" ","_"))

import re

# 472-518
if __name__ == '__main__':

    dir = 'E:\\file\\xmla_audio\\'
    dirs = ['摸金天师']#,'月亮与六便士' , '巴黎圣母??',,
    for d in dirs:
        li = file_name(dir + d)
