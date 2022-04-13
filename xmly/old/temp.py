# -*- coding: UTF-8 -*-


def merge(srcList,dest):

    lines = []
    for src in srcList:
        with open(src,'r',encoding='utf-8')as f:
            lines += f.readlines()

    with open(dest,'w',encoding='utf-8')as f:
        f.writelines(lines)
if __name__ == '__main__':
    srclist = ["1.txt","2.txt","3.txt"]
    dest = "0.txt"
    merge(srclist,dest)