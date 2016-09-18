import cv2
import numpy as np
import os

pic_num = 1000

if not os.path.exists('pos'):
        os.makedirs('pos')

with open("positives.txt", "r") as ins:
    array = []
    for lineWrapped in ins:
        line = lineWrapped.rstrip('\n')
        print(line)
        img = cv2.imread(line,cv2.IMREAD_GRAYSCALE)
        print(img)
        # should be larger than samples / pos pic (so we can place our image on it)
        resized_image = cv2.resize(img, (50, 50))
        cv2.imwrite("pos/A_"+str(pic_num)+".png",resized_image)
        pic_num += 1

