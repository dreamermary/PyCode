# -*- coding: utf-8 -*-
# @Author  :   clumba
# @File    :   cutting_bstc.py
# @Time    :   2021/4/21 10:26
'''
    clip
        ...wav
    train.tsv
    dev.tsv
'''


# read
import argparse
import json

# fp = ""
# with open(fp,"r")as f:
#     lines = f.readlines()
#     for li in lines:
#         jli = json.loads(li.rstrip())


# cut & write
import os

import soundfile


def split_file(file_path, new_file_path, start_time, duration):
    """

    :param file_path:
    :param new_flac_path:
    :param start_time:
    :param end_time:
    :return:
    """
    sf = soundfile.SoundFile(file_path)
    data = sf.read()
    end_time = float(start_time) + float(duration)
    start, end = int(float(start_time) * sf.samplerate), int(float(end_time) * sf.samplerate) + 1
    # print start, end, float(start_time) * sf.samplerate, float(end_time) * sf.samplerate
    soundfile.write(open(new_file_path, "wb"), data[start:end], 16000, format="WAV")



def cut_wav(corpus_root,transcript_path,split):

    tt = []
    for idx,line in enumerate(open(transcript_path,encoding='utf-8').readlines()):
        line = line.strip()
        item = json.loads(line)
        wav = item.get("wav")
        wav_path = os.path.join(corpus_root,split,"wav", wav)
        if not os.path.exists(wav_path):
            raise ValueError("File not found in %s" % wav_path)
        new_wav_path = os.path.join(corpus_root,split,"cutting", wav.replace(".wav", "_%s.wav" % idx))

        split_file(wav_path, new_wav_path, item.get("offset"), item.get("duration"))

        j = '{"client_id":"%s","path":"%s","sentence":"%s","split":"%s","translation":"%s"}\n'\
            %(item.get('speaker'),wav.replace(".wav", "_%s.wav" % idx),item.get("transcript"),split,item.get("translation"))
        tt.append(j)
    return tt

def main(corpus_root,split):
    tsv = []
    transcript_root = os.path.join(corpus_root,split,"transcripts")

    for dirpath, dirnames, filenames in os.walk(transcript_root):
        for name in filenames:
            if '.json' in name:
                transcript_path = os.path.join(transcript_root,name)
                tt = cut_wav(corpus_root,transcript_path,split)
                tsv += tt
    with open(os.path.join(corpus_root,s,s+'.tsv'),'a',encoding='utf-8')as f:
        f.writelines(tsv)

def prepare(corpus_root,split):
    for s in split:
        cutting_path = os.path.join(corpus_root,s,"cutting")
        trans_tsv_path = os.path.join(corpus_root,s,s+'.tsv')
        if not os.path.exists(cutting_path):
            os.mkdir(cutting_path)
        if not os.path.exists(trans_tsv_path):
            open(trans_tsv_path,'w')

SPLIT = ["train","dev","apply_16k"]


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--corpus_root_path', help='', default=r'E:\test')
    args = parser.parse_args()

    corpus_root = args.corpus_root_path
    split =  ["train"]
    prepare(corpus_root,split)
    for s in split:
        main(corpus_root,s)


