# -*- coding: utf-8 -*-
import pyaudio
import sys
import asyncio
import websockets
import json
import time
import _thread

HOST = '222.197.219.18'
uri = "ws://222.197.219.18:12362"
PORT = 12362
BUFSIZ =1024
RATE = 16000
CHUNK = 1024
key = "ivan"

pa = pyaudio.PyAudio()
stream = pa.open(format=pyaudio.paInt16, channels=1, rate=RATE, input=True,start=False,frames_per_buffer=1024) #8000

async def hello():
    async with websockets.connect(uri) as websocket:    # 创建连接
        asyncio.create_task(on_message(websocket))      # 创建监听
        await websocket.send(json.dumps({               # 同步发送-开始符
            "signal": "start",
            "nbest": 1,
            "continuous_decoding": True
          }))
        stream.start_stream()
        while(True):
            string_audio_data = stream.read(CHUNK) #16000
            await websocket.send(string_audio_data)     # 同步发送音频
            
            

        stream.stop_stream()
        stream.close()
        pa.terminate()

async def on_message(ws):
    print("on_message")
    while(True):
        re = await ws.recv()
        print(re)

asyncio.get_event_loop().run_until_complete(hello())


