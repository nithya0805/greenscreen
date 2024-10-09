import cv2
import time
import numpy as np

# list = ["nithya",11,True]
#array = [10,5,4,60,86]


#loading the video

rawvideo = cv2.VideoCapture("video.mp4")

time.sleep(1)

#count is the number of frames in the video
count = 0
background = 0 
# background is the initial frame of the video which we want to capture

