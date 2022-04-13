import argparse
import os
from concurrent.futures.thread import ThreadPoolExecutor


def add_wav_list(path,lines):
    with open(path,'a',encoding='utf-8')as f:
        f.writelines(lines)


# 读取一个字幕文件返回时间戳列表
def get_stamps(path):
    stamps_list = []
    subtitle_list = []
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

                subtitle_list.append(lines[4*i+2].rstrip())
    except:
        pass
    #     stamps_list = []
    #     with open("D:\\temp_file\\鬼吹灯\\text\\error.log", "a",encoding="utf-8")as f:
    #         f.write(path+":"+"no this file\n")
    return stamps_list,subtitle_list

def cut(cmd_list):
    for i in cmd_list:
        os.system(i)


def cut_piece(file_dir):
    pool = ThreadPoolExecutor(max_workers=10)
    thread_list = []
    count = 0
    for dirpath, dirnames, filenames in os.walk(os.path.join(file_dir,"output")):
        for dirname in dirnames:
            path_text = os.path.join(file_dir, "text", dirname+".srt")
            path_audio = os.path.join(file_dir, "output", dirname, "vocals.wav")
            path_output = os.path.join(file_dir,"cutting",dirname)
            stamps_list,subtitle_list = get_stamps(path_text)
            file_list = []
            if "鬼吹灯之龙岭迷窟" not in path_text:
                 continue
            cmd_list = []
            for j,(stamps,subtitle) in enumerate(zip(stamps_list,subtitle_list),1): # '+path_audio+'  '+stamps[0]+''+stamps[1]+
                tmp_out = path_output+("_%05d"%j)+".wav"
                cmd = "ffmpeg  -i  %s  -vn -acodec copy -ss  %s   -to  %s  %s "%(path_audio,stamps[0],stamps[1],tmp_out)
                # os.system(cmd)

                cmd_list.append(cmd)
            trd = pool.submit(cut, cmd_list)
            thread_list.append(trd)

                # tmp_path = os.path.join(os.path.split(os.path.split(os.path.split(tmp_out)[0])[0])[-1],os.path.split(os.path.split(tmp_out)[0])[-1],os.path.split(tmp_out)[-1])
                # file_list.append("%s\t\t%s\n"%(tmp_path,subtitle))
            # add_wav_list(args.wav_list_path,file_list)
            print("ffmpeg finished: %s"% path_text)
            count += 1
        print("------------count:%s------------"%count)
        break
    print([i.result() for i in thread_list])
    pool.shutdown()



parser = argparse.ArgumentParser()
parser.add_argument("--save_root", default=r"D:\temp_file", type=str)
parser.add_argument("--wav_list_path", default="E:\\file\\xmla_audio\\gcd.wav.lst", type=str)

if __name__ == '__main__':
    args = parser.parse_args()

    dir = args.save_root
    for d in ["鬼吹灯"]:
        li = cut_piece(os.path.join(dir, d))
    print("------------ok------------")
