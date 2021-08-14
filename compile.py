import cv2
import numpy as np
import glob
import re, os

img_array = []
numbers = re.compile(r'(\d+)')
def numericalSort(value):
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts

for filename in sorted(glob.glob('./frames/frame*.jpg') , key=numericalSort):
    if os.path.exists(filename.replace("\\","/")):
        print(filename.replace("\\","/"))
        img = cv2.imread(filename.replace("\\","/"))
        try:
            height, width, layers = img.shape
            size = (width,height)
            img_array.append(img)
        except Exception as e:
            continue

print(len(img_array))
out = cv2.VideoWriter('./output.mp4',cv2.VideoWriter_fourcc(*'mp4v'), 20.0, size)

for i in range(len(img_array)):
    out.write(img_array[i])

out.release()
