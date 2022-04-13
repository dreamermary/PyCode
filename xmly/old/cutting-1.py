import os

# 读取一个字幕文件返回时间戳列表
def get_stamps(path):
    stamps_list = []
    try:
        with open(path,encoding="utf-8")as f:
            lines = f.readlines()
            for i in range(0,(len(lines)//4),1):
                li = lines[4*i+1]
                stamp = li.split(" --> ")
                start = stamp[0].rstrip()
                end = stamp[1].rstrip()
                stamps = [start.replace(',','.'),end.replace(',','.')]
                stamps_list.append(stamps)
    except:
        stamps_list = []
        with open("D:\\temp_file\\海底两万里\\text\\error.log", "a",encoding="utf-8")as f:
            f.write(path+":"+"no this file\n")
    return stamps_list


# ffmpeg  -i source.mp3  -vn -acodec copy -ss 00:03:21.36 -t 00:00:41 output.mp3






def file_name(file_dir):
    for dirpath, dirnames, filenames in os.walk(file_dir):
        for i in filenames:
            path_text = file_dir+'\\text\\'+i.split(".")[0]+'.zh-cn.srt'
            path_audio = file_dir+'\\output\\'+i.split(".")[0]+'\\vocals.wav'
            # if '.srt' in path_text:

            # cmd1 = "cd E:\\softdata\\pycharm\\venv\\crawler\\Lib\\site-packages\\spleeter "
            # cmd2 = "spleeter separate -p spleeter:2stems -o "+file_dir+"\\output"+"  "+path+" -d 3600"
            # os.system(cmd1+" && "+cmd2)

            stamps_list = get_stamps(path_text)
            for j,stamps in enumerate(stamps_list):
                cmd = 'ffmpeg  -i '+path_audio+'  -vn -acodec copy -ss '+stamps[0]+' -to '+stamps[1]+' '+file_dir+'\\cutting\\'+i.split(".")[0]+'_'+str(j)+'.wav'
                os.system(cmd)
                print(cmd)






if __name__ == '__main__':
    dir = 'D:\\temp_file\\'
    dirs = ['海底两万里']#, '海底两万里', '摸金天师', '海底两万里', '鬼吹灯'
    for d in dirs:
        li = file_name(dir + d)
