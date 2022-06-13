import time
import threading
import sys
import nls
import json
# from test_wav2pcm import wav2pcm
import multiprocessing
import os
from struct import *

__all__ = ["wav2pcm"]
CHUNK = 1024
import pyaudio
RATE = 16000
# nls.enableTrace(True)

URL = "ws://222.197.219.7:8101/ws/v1"
APPKEY = "default"
TOKEN = "default"


class TestSr:
    def __init__(self, tid, test_file, trans):
        # self.__th = threading.Thread(target=self.__test_run)
        self.__id = tid
        self.__test_file = test_file
        self.trans = trans

    def loadfile(self, filename):
        self.__data = wav2pcm(filename)
        pass

    def start(self):
        self.loadfile(self.__test_file)
        self.__test_run()

    def test_on_start(self, message, *args):
        # print("test_on_start:{}".format(message))
        pass

    def test_on_error(self, message, *args):
        # print("on_error args=>{}".format(args))
        pass

    def test_on_close(self, *args):
        # print("on_close: args=>{}".format(args))
        pass

    def test_on_result_chg(self, message, *args):
        # print("test_on_chg:{}".format(message))
        pass

    def test_on_completed(self, message, *args):
        d = json.loads(message)
        print(d['payload']['result'])

    def __test_run(self):
        print("thread:{} start..".format(self.__id))

        sr = nls.NlsSpeechRecognizer(
            url=URL,
            # akid=AKID,
            # aksecret=AKKEY,
            appkey=APPKEY,
            token=TOKEN,
            on_start=self.test_on_start,
            on_result_changed=self.test_on_result_chg,
            on_completed=self.test_on_completed,
            on_error=self.test_on_error,
            on_close=self.test_on_close,
            # callback_args=[self.__id]
        )
        print("{}: session start".format(self.__id))
        r = sr.start(aformat="pcm", ex={"hello": 123})

        self.__slices = zip(*(iter(self.__data),) * 640)

        for i in self.__slices:
            sr.send_audio(bytes(i))
            time.sleep(0.01)

        r = sr.stop()
        print("{}: sr stopped:{}".format(self.__id, r))
        time.sleep(1)


def wav2pcm(wavfile):
    with open(wavfile, "rb") as i:
        i.seek(0)
        _id = i.read(4)
        _id = unpack('>I', _id)
        _size = i.read(4)
        _size = unpack('<I', _size)
        print("size={}".format(_size))
        _type = i.read(4)
        _type = unpack(">I", _type)
        if _id[0] != 0x52494646 or _type[0] != 0x57415645:
            raise ValueError("not a wav!")
        i.read(32)
        result = i.read()
        return result


t = TestSr("test", "xx.wav", [])
t.start()
