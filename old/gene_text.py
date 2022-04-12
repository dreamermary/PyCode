import os

# 计算该文件所有音频时??
def file_name(file_dir):
    for dirpath, dirnames, filenames in os.walk(file_dir):
        for i in filenames:
            path = file_dir+'\\'+i
            cmd1 = "cd D:\\com\\autosub-0.5.7-alpha-win-x64-pyinstaller\\autosub_pyinstaller "
            ipath = path
            opath = file_dir + '\\text'
            cmd3 = "autosub -S zh-CN -D zh-CN -i "+ipath+" -o "+opath
            cmd = cmd1+" && "+cmd3
            # os.system(cmd)
            os.system(cmd1)
            print(path)
        break

            # print(cmd1)
            # print(cmd2)
            # os.rename(path, path.replace(" ","_"))
            # print(path.replaceAll(" ","_"))

import re

if __name__ == '__main__':

    dir = 'E:\\file\\xmla_audio\\'
    dirs = ['月亮与六便士']#,'摸金天师' ,,'海底两万里' ,,
    for d in dirs:
        li = file_name(dir + d)
