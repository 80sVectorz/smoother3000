import shutil,os
if os.path.exists("frames/"):
    print("removing folder")
    shutil.rmtree('frames/')
    os.mkdir("frames/")


import cv2
import numpy as np

def mse(imageA, imageB):
	# the 'Mean Squared Error' between the two images is the
	# sum of the squared difference between the two images;
	# NOTE: the two images must have the same dimension
	err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
	err /= float(imageA.shape[0] * imageA.shape[1])

	# return the MSE, the lower the error, the more "similar"
	# the two images are
	return err

vidcap = cv2.VideoCapture('2021-08-14 15-45-09.mp4')
success,image = vidcap.read()
count = 0
while success:
    lastFrame=image
    #save frame as JPEG filename
    success,image = vidcap.read()
    if success:
        if mse(image, lastFrame) > 10.0:
            print(mse(image, lastFrame))
            cv2.imwrite("./frames/frame%d.jpg" % count, image)
            print('Read a new frame: ', success)
    count += 1
