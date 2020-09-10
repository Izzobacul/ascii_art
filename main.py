#!/usr/bin/env python3

from PIL import Image
from cv2 import VideoCapture
import sys


def to_ascii(im):
    chars = [' ', '.', "'", '`', '\\', '^', '"', ',', ':', ';', 'I', 'l', '!', 'i', '>', '<', '~', '+', '_', '-', '?', ']', '[', '}', '{', '1', ')', '(', '|', '\\', '/', 't', 'f', 'j', 'r', 'x', 'n', 'u', 'v', 'c', 'z', 'X', 'Y', 'U', 'J', 'C', 'L', 'Q', '0', 'O', 'Z', 'm', 'w', 'q', 'p', 'd', 'b', 'k', 'h', 'a', 'o', '*', '#', 'M', 'W', '&', '8', '%', 'B', '@', '$']
    #chars = ['$', '@', 'B', '%', '8', '&', 'W', 'M', '#', '*', 'o', 'a', 'h', 'k', 'b', 'd', 'p', 'q', 'w', 'm', 'Z', 'O', '0', 'Q', 'L', 'C', 'J', 'U', 'Y', 'X', 'z', 'c', 'v', 'u', 'n', 'x', 'r', 'j', 'f', 't', '/', '\\', '|', '(', ')', '1', '{', '}', '[', ']', '?', '-', '_', '+', '~', '<', '>', 'i', '!', 'l', 'I', ';', ':', ',', '"', '^', '\\', '`', "'", '.', ' ']
    prop = im.size[1] / im.size[0]
    if im.size[0] > 1024:
        im = im.resize((1024, int(1024*prop)))
    elif im.size[1] > 512:
        im = im.resize((im.size[1]/prop, 512))
    data = im.load()
    width, height = im.size
    out = ""
    for i in range(height):
        for j in range(width):
            value = sum(data[j, i])
            out += chars[int(value/765*70)]
        out += '\n'
    return out

def main(input_path, output):
    if input_path == 'camera':
        cam = VideoCapture(0)
        s, img = cam.read()
        img = Image.fromarray(img)
        if not s:
            return
    else:
        img = Image.open(input_path)
    asci = to_ascii(img)
    with open(output, 'w') as out:
        out.write(asci)
    return
    

if __name__ == '__main__':

    inp = sys.argv[1]
    output = sys.argv[2]
    main(inp, output)