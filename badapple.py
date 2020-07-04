# -*- coding:utf8 -*-

from PIL import Image
import time


def draw(img):
    w = 0
    mw = img.width
    str = ""
    for pixel in iter(img.getdata()):
        # print(pixel)
        if(w == mw):
            w = 0
            str += "\n"
        w += 1
        if(pixel == 0):
            str += "  "
        else:
            str += "##"
    print(str+'\033[30A')


t = time.time()
for i in range(1, 6572):
    im = Image.open("./bad-apple/img"+str(i)+".png")
    draw(im)
    while time.time() < (t+(1/30*i)):
        time.sleep(0.001)
