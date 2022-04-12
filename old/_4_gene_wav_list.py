import os

# 读取一个字幕文件返回时间戳列表
def get_text(path):
    text_list = []
    try:
        with open(path,encoding="utf-8")as f:
            lines = f.readlines()
            for i in range(0,(len(lines)//4),1):
                li = lines[4 * i + 2]
                text_list.append(li)
    except:
        stamps_list = []
        with open("D:\\temp_file\\巴黎圣母院\\text\\error_text.log", "a",encoding="utf-8")as f:
            f.write(path+":"+"no this file\n")
    return text_list


# ffmpeg  -i source.mp3  -vn -acodec copy -ss 00:03:21.36 -t 00:00:41 output.mp3






def file_name(file_dir):
    wav_list =[]
    last_file_name = ""
    cur_text_list = []
    idx = 0
    try:
        for dirpath, dirnames, filenames in os.walk(file_dir+'\\cutting'):
            for i in filenames:
                if (i.split('_')[0] != last_file_name):
                    last_file_name = i.split('_')[0]
                    cur_text_list = get_text(file_dir+'\\text\\'+last_file_name+'.srt')
                    idx = 0

                wav_list.append("巴黎圣母院"+'\\'+i + '\t' + cur_text_list[idx])
                idx += 1
    except:
        print(idx)
        print(i)
        print()
        print(str(i) + str('\t') + cur_text_list[idx])
    return wav_list






if __name__ == '__main__':
    dir = 'D:\\temp_file\\'
    dirs = ['巴黎圣母院']#, '巴黎圣母院', '摸金天师', '海底两万里', '鬼吹灯'
    wav_list = []
    for d in dirs:
        wav_list = file_name(dir + d)

    with open("D:\\temp_file\\wav.lst",'a',encoding='utf-8')as f:
        f.writelines(wav_list)


