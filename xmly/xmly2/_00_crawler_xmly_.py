import re
from concurrent.futures.thread import ThreadPoolExecutor

import requests
import os
import json
import argparse

import urllib3

root = ''
ialbum = ''
album = ''
oalbum = ''

import utils
def prepare(args):
    ls = []
    with open(args.ialbum, 'r+',encoding='utf-8')as f:
        lines = f.readlines()
        for li in lines:
            arr = li.split(' ')
            name = arr[0].replace(' ', "_")
            name = name.replace('|', "_")
            name = name.replace('｜', "_")
            print("hh:",name,arr)
            ls.append(f'{name}\t{arr[1]}')
            if not os.path.exists(os.path.join(args.save_root,name)):
                os.makedirs(os.path.join(args.save_root,name))
    with open(args.album, 'w', encoding='utf-8')as fw:
        fw.writelines(ls)


def get_response(html_url):
    header = {
        # 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36',
        # 'Cookie':''
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36',
    }
    urllib3.disable_warnings()
    try:
        response = requests.get(url=html_url, headers=header,verify=False)
    except :
        print('--------'+html_url)
    return response

def download_and_save(dir, title, audio_url):
    if not os.path.exists(dir):
        os.makedirs(dir)
    audio_content = get_response(audio_url).content

    # title_modified = alter_title(title)
    title_modified = title.replace(" ","_")

    with open(os.path.join(dir, title_modified + '.m4a'), mode='wb') as f:
        f.write(audio_content)
        print('正在保存：new name:%s \n\t old name:%s \n\n'%(title_modified,title))
    return 0

def get_audio_info(html_url):

    audio_info_list = []
    content = json.loads(get_response(html_url).text)
    jlist = content['data']['trackDetailInfos']
    durations = 0
    for li in jlist:

        # 音频ID
        audio_id = li['id']
        # 章节名字
        audio_title = li['trackInfo']['title']
        # 下载地址
        audio_url = li['trackInfo']['playPath']
        duration = li['trackInfo']['duration']
        durations += duration

        audio_info = []
        audio_info.append(audio_id)
        audio_info.append(audio_title)
        audio_info.append(audio_url)

        audio_info_list.append(audio_info)


    return audio_info_list,durations

    # albumids = ['30748094','23085924','4756811','33620874']
    # dirs = ['月亮与六便士','巴黎圣母院','摸金天师','海底两万里','鬼吹灯']



parser = argparse.ArgumentParser()
parser.add_argument("--save_root", default="F:\\xmly_03", type=str)
parser.add_argument("--ialbum", default="ialbum.txt", type=str)
parser.add_argument("--album", default="album.txt", type=str)
parser.add_argument("--oalbum", default="oalbum.txt", type=str)

# https://audiopay.cos.tx.xmcdn.com/download/1.0.0/group3/M08/8D/E3/wKgMdl3FLbSTIh6rADrEkWjiB_o705.m4a?sign=b299e87642ca0a9a8d0525553f9c1a2a&buy_key=FM&token=3475&timestamp=1623329588&duration=1244

def main():

    pool = ThreadPoolExecutor(max_workers=5)
    args = parser.parse_args()

    prepare(args)

    pagesize = 50
    oalbum = []

    thread_list = []
    for line in open(args.album,'r',encoding='utf-8').readlines():
        album_name,album_id = line.split('\t')
        # get audio_info of a album
        page = 1
        audio_info_list = []
        album_durations = 0
        while True:
            url = f'https://m.ximalaya.com/m-revision/common/album/queryAlbumTrackRecordsByPage?albumId={album_id.strip()}&page={page}&pageSize={pagesize}&asc=true&countKeys=play%2Ccomment&v=1623377038200'
            temp_list,durs = get_audio_info(url)
            if len(temp_list) > 0:
                audio_info_list += temp_list
                page += 1
            else:
                break
            album_durations += durs
        oalbum.append(f"{album_name}\t{album_durations}\t{album_id}")

        # download & save
        for li in audio_info_list:
            file_path = os.path.join(args.save_root, album_name)
            trd = pool.submit(download_and_save,file_path, li[1], li[2])
            thread_list.append(trd)
            print("Thread added: %s"  % file_path)

    with open (args.oalbum,'w',encoding='utf-8')as f:
        f.writelines(oalbum)
    print([i.result() for i in thread_list])
    pool.shutdown()

## 下载文件名-空格替换
## 章节数有序 - 占位
if __name__ == '__main__':
    main()
    # args = parser.parse_args()
    # prepare(args)