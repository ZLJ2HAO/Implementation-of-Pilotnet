import cv2
from PIL import Image
import numpy as np
import glob
import os

image_list = []
path = "/home/roy/Implementation-of-Pilotnet/new_img/"
folder = "/home/roy/Implementation-of-Pilotnet/crop_img"
cnt = 0
def do_canny():
    global cnt
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        edge = cv2.Canny(img, 180, 200)
        #fname = os.path.splitext(filename)[0]
        #ext = os.path.splitext(filename)[1]
        cv2.imwrite(os.path.join(path, filename), edge)
        print("Writing", filename)
        cnt = cnt + 1
        # if cnt >= 10:
        #    exit()

if __name__ == '__main__':
    try:
        do_canny()
    except KeyboardInterrupt:
        exit()
