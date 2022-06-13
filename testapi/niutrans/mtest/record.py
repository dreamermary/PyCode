import time
import threading
import sys
import nls
import json
# from test_wav2pcm import wav2pcm
import multiprocessing
import os
from struct import *
import  wave
from datetime import datetime, timedelta
# __all__ = ["wav2pcm"]
CHUNK = 1024
import pyaudio
RATE = 16000

'''开始录音'''
pa = pyaudio.PyAudio()
stream = pa.open(format=pyaudio.paInt16, channels=1, rate=RATE, input=True, start=False,
                 frames_per_buffer=1024)  # 8000
stream.start_stream()

'''指定秒数'''
INTERVAL = timedelta(seconds=5)
last_checked = datetime.now() - INTERVAL

frames = []
last_checked = datetime.now()
for i in range(500):
    now = datetime.now()
    if INTERVAL <= (now - last_checked):
        break

    data = stream.read(CHUNK)  # 16000
    frames.append(data)

stream.stop_stream()
stream.close()
pa.terminate()

'''写音频二进制流'''
# with open('xx','wb')as f:
#     for i in frames:
#         f.write(i)

'''写wav'''
wf = wave.open("xx.wav", 'wb')
wf.setnchannels(1)
wf.setsampwidth(pa.get_sample_size(pyaudio.paInt16))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()

'''wav2pcm'''
# from struct import *
# __all__=["wav2pcm"]
# def wav2pcm(wavfile, pcmfile):
#     with open(wavfile, "rb") as i, open(pcmfile, "wb") as o:
#         i.seek(0)
#         _id = i.read(4)
#         _id = unpack('>I', _id)
#         _size = i.read(4)
#         _size = unpack('<I', _size)
#         print("size={}".format(_size))
#         _type = i.read(4)
#         _type = unpack(">I", _type)
#         if _id[0] != 0x52494646 or _type[0] != 0x57415645:
#             raise ValueError("not a wav!")
#         i.read(32)
#         result = i.read()
#         o.write(result)
# wav2pcm("xx.wav","xx.pcm")