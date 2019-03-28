import cv2
from PIL import Image
import numpy as np
import glob
import os

image_list = []
path = "/home/roy/Implementation-of-Pilotnet/crop_img/"
folder = "/home/roy/Implementation-of-Pilotnet/IMG"
cnt = 0
def do_crop():
    global cnt
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        crop_img = img[60:150, :]
        cv2.imwrite(os.path.join(path, filename), crop_img)
        print("Writing", filename)
        cnt = cnt + 1


if __name__ == '__main__':
    try:
        do_crop()
    except KeyboardInterrupt:
        exit()
