import argparse
import os
from concurrent.futures.thread import ThreadPoolExecutor

from xmly.xmly2 import utils


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


def cut_piece(file_dir):
    for dirpath, dirnames, filenames in os.walk(os.path.join(file_dir,"split")):
        for dirname in dirnames:
            path_text = os.path.join(file_dir, "text", dirname+".srt")
            path_audio = os.path.join(file_dir, "split", dirname, "vocals.wav")
            path_output = os.path.join(file_dir,"cutting",dirname)
            stamps_list,subtitle_list = get_stamps(path_text)
            file_list = []
            for j,(stamps,subtitle) in enumerate(zip(stamps_list,subtitle_list),1): # '+path_audio+'  '+stamps[0]+''+stamps[1]+
                tmp_out = path_output+("_%05d"%j)+".wav"
                cmd = "ffmpeg  -i  %s  -vn -acodec copy -ss  %s   -to  %s  %s "%(path_audio,stamps[0],stamps[1],tmp_out)
                os.system(cmd)

                tmp_path = os.path.join(os.path.split(os.path.split(os.path.split(tmp_out)[0])[0])[-1],os.path.split(os.path.split(tmp_out)[0])[-1],os.path.split(tmp_out)[-1])
                file_list.append("%s\t\t%s\n"%(tmp_path,subtitle))
            add_wav_list(args.wav_list_path,file_list)
            print("ffmpeg finished: %s"% path_text)




parser = argparse.ArgumentParser()
parser.add_argument("--save_root", default="F:\\xmly", type=str)
parser.add_argument("--album_path", default="album.json", type=str)
parser.add_argument("--wav_list_path", default="F:\\xmly\\wav.list", type=str)

def main():
    pool = ThreadPoolExecutor(max_workers=10)
    thread_list = []
    args = parser.parse_args()

    dir = args.save_root
    dirs = utils.read_album_name_json(args.album_path)  # ['鬼吹灯', '巴黎圣母院']
    for d in dirs:
        # li = cut_piece(os.path.join(dir, d))

        path = os.path.join(dir, d)
        trd = pool.submit(cut_piece,path)
        thread_list.append(trd)
        print("Thread added: %s" % path)
        # download_and_save(os.path.join(args.save_root, album_name, "origin"), li[1], li[2])
    print([i.result() for i in thread_list])
    pool.shutdown()

if __name__ == '__main__':
    main()
