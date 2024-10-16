import cv2
import time
import numpy as np

# list = ["nithya",11,True]
#array = [10,5,4,60,86]


#loading the video

rawvideo = cv2.VideoCapture("video.mp4")

time.sleep(1)
# sleep is too make sure the python code doesnt start unless the image is loaded

#count is the number of frames in the video
count = 0
backgroundimg = 0 
# background is the initial frame of the video which we want to capture


for i in range(60):
    #reading one frame at a time from our raw video
    status,backgroundimg=rawvideo.read()
    # read if the function that is going to give us the status and the frame as an image
    #status is the  variable tht stores the true or false depending on if their are any frames available or not
    #background is the variable storing the frame
     
    if status == False:
        continue

backgroundimg = np.flip(backgroundimg,axis=1)
#npflip , the recording happens in reverse so the flip makes sure its acc in the right direction as when recording the video its flippped
# axis = 0 is y axis and axis = 1 is x axis.

while rawvideo.isOpened():

    status,image = rawvideo.read()
    # if status becomes false then thers no status left , so video wont run further.
    if not status :
        break

    count = count + 1

    image = np.flip(image,axis=1)
    #flipping image and storing in same variable
    
    #HSV - hue saturation and value(diff colour scheme that we use for scans)#

    HSV_img = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    red_left = np.array([100,40,40 ])
    red_top = np.array([100,255,255])

    mask1 = cv2.inRange(HSV_img , red_left,red_top)
# minimum possible
    red_right = np.array([155,40,40])
    red_bottom = np.array([180,255,255])

    mask2 = cv2.inRange(HSV_img , red_right,red_bottom)
    #max value

    mask1 = mask1 + mask2
#for refining the image as raw and blur after processing it HSV format


    
#homework = work on collage
