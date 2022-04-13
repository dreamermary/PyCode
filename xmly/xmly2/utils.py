import os
import json

def read_album_json(file):
    '''
    read a json file ,which contain album_id and album_name,return generator which (id,name)
    :param file:str,
    :return: tuple(str,str),iterative return (id,name)
    '''

    with open("album.json", "r") as f:
        load_json = json.load(f)
        for li in load_json:
            yield li.items()


def read_album_name_json(file):
    '''
    read a json file ,which contain album_id and album_name,return generator which (id,name)
    :param file:str,
    :return: tuple(str,str),iterative return (id,name)
    '''
    list_name = []
    with open("album.json", "r") as f:
        load_json = json.load(f)
        for li in load_json:
            list_name.append(li['name'])
    return list_name


'''
    trans hanzi_shuzi to alb_shuzi.
    eg:二十八 -> 28
'''
common_used_numerals_tmp ={'零':0, '一':1, '二':2, '两':2, '三':3, '四':4, '五':5, '六':6, '七':7, '八':8, '九':9, '十':10, '百':100, '千':1000, '万':10000, '亿':100000000}
common_used_numerals = {}
for key in common_used_numerals_tmp:
    common_used_numerals[key.encode('gbk').decode('cp936')] = common_used_numerals_tmp[key]
def chinese2digits(uchars_chinese):
    total = 0
    r = 1              #表示单位：个十百千...
    for i in range(len(uchars_chinese) - 1, -1, -1):
        val = common_used_numerals.get(uchars_chinese[i])
        if val >= 10 and i == 0:  #应对 十三 十四 十*之类
            if val > r:
                r = val
                total = total + val
            else:
                r = r * val
            #total =total + r * x
        elif val >= 10:
            if val > r:
                r = val
            else:
                r = r * val
        else:
            total = total + r * val
    return total

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
