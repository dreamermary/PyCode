# -*- coding: utf-8 -*-
# @Author  :   clumba
# @File    :   filiter.py
# @Time    :   2022/4/11 21:28

# acl21
conf = 'acl'
year = '21'
finame = f'../file_{conf}{year}_all_md.txt'
foname1 = f'./{year}_{conf}_speech.txt'
foname2 = f'./{year}_{conf}_translation.txt'
lnss1,lnss2 = [],[]
with open(finame,encoding='utf-8')as fi:
    lns = fi.readlines()
    for li in lns:
        if ('speech'  in li)or ('Speech'  in li):
            lnss1.append(li)
        if ('Translation'  in li)or ('translation'  in li):
            lnss2.append(li)
with open(foname1,'w',encoding='utf-8')as fo:
    fo.writelines(lnss1)
with open(foname2,'w',encoding='utf-8')as fo:
    fo.writelines(lnss2)
