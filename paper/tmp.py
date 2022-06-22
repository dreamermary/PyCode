import re
_ls = []
with open('./ref.txt','r',encoding='gbk')as f:
    ls = f.readlines()
    for li in ls:
        li = re.sub("\[[0-9]+\]","",li)
        _ls.append(li)

with open('./ref.txt2','w',encoding='gbk')as f:
    f.writelines(_ls)
