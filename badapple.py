# -*- coding:utf8 -*-

import time
import gzip

import threading

class MP3(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.mp3='bad_apple.mp3'
        self.setDaemon(True)
    def run(self):
        playsound(self.mp3)

def draw(data):
    w = 0
    mw = 40
    string = ""
    for pixel in data:
        if(w == 40):
            w = 0
            string += "\n"
        w += 1
        if(pixel == 0):
            string += "  "
        else:
            string += "##"
    print(string+'\033[30A')


t = time.time()
i = 0
try:
    from playsound import playsound
    mp3=MP3()
    mp3.start()
except:
    pass

try:
    size = 1200
    with gzip.open('bad-apple.dat.gz') as f:
        while i < 6573:
            i = int((time.time()-t)*30)+1
            f.seek(i*size)
            draw(f.read(1200))
            time.sleep(0.02)
except KeyboardInterrupt:
    print(""+'\033[30B')
