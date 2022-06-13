import time
import threading
import sys

import nls
import json



CHUNK = 1024
import pyaudio
RATE = 16000

URL = "ws://222.197.219.7:8101/ws/v1"
APPKEY = "default"
TOKEN = "default"



class TestSt:
    def __init__(self):
        pass

    def start(self):
        self.__test_run()

    def test_on_sentence_begin(self, message, *args):
        # print("test_on_sentence_begin:{}".format(message))
        pass
    def test_on_sentence_end(self, message, *args):
        # print("test_on_sentence_end:{}".format(message))
        # print(f'end:{msg["payload"]["result"]}')
        msg = json.loads(message)
        print(f'{msg["payload"]["result"]}')

    def test_on_start(self, message, *args):
        # print("test_on_start:{}".format(message))
        pass

    def test_on_error(self, message, *args):
        # print("on_error args=>{}".format(args))
        pass
    def test_on_close(self, *args):
        # print("on_close: args=>{}".format(args))
        pass

    def test_on_result_chg(self, message, *args):   ## 中间结果
        # print("test_on_chg:{}".format(message))
        # msg = json.loads(message)
        # print(f'chg:{msg["payload"]["result"]}')
        pass
    def test_on_completed(self, message, *args):
        # print("on_completed:args=>{} message=>{}".format(args, message))
        pass

    def __test_run(self):
        sr = nls.NlsSpeechTranscriber(
                    url=URL,
                    # akid=AKID,
                    # aksecret=AKKEY,
                    appkey=APPKEY,
                    token=TOKEN,
                    on_sentence_begin=self.test_on_sentence_begin,
                    on_sentence_end=self.test_on_sentence_end,
                    on_start=self.test_on_start,
                    on_result_changed=self.test_on_result_chg,
                    on_completed=self.test_on_completed,
                    on_error=self.test_on_error,
                    on_close=self.test_on_close,
                    # callback_args=[self.__id]
                )

        pa = pyaudio.PyAudio()
        stream = pa.open(format=pyaudio.paInt16, channels=1, rate=RATE, input=True, start=False,
                         frames_per_buffer=1024)  # 8000
        stream.start_stream()

        while True:
            print("请开始讲话：")
            r = sr.start(aformat="pcm",
                         enable_intermediate_result=True,)
                         # enable_punctutation_prediction=True,
                         # enable_inverse_text_normalization=True)

            while True:
                string_audio_data = stream.read(1024)
                sr.send_audio(string_audio_data)
                time.sleep(0.01)

            sr.ctrl(ex={"test":"tttt"})
            time.sleep(1)

            r = sr.stop()
            print("{}: sr stopped:{}".format(self.__id, r))
            time.sleep(5)

t = TestSt()
t.start()


