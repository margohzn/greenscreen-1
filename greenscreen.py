import cv2
import numpy as np
import time

video = cv2.VideoCapture("video.mp4")

time.sleep(1)
count = 0 
background = 0

for i in range(60):
    status, background = video.read() #read fonction used to read each frame in video 
    #status video.read fonction gives status of the frame 
    #background is a varaible in which we are storing the frame we recive
    if status == False:
        continue

#flipping the background image left right fliping
background = np.flip(background, axis = 1)
 
while video.isOpened():
    status, frame = video.read()
    if status == False:
        break
    np.flip(frame, axis = 1)
    count += 1
    #converting frame to HSV color format
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #color range for masking (HSV) hue, saturation, value
    low_red1 = np.array([100,40,40])
    low_red2 = np.array([100,255,255])
    mask1 = cv2.inRange(hsv, low_red1, low_red2)
    upper_red1 = np.array([155,40,40])
    upper_red2 = np.array([180,255,255])
    mask2 = cv2.imRange(hsv, upper_red1, upper_red2)
    mask = mask1 + mask2

    #refining the mask 
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3,3), np.uint8), iterations = 2)
    mask = cv2.dilate(mask, np.ones((3,3), np.uint8), iterations = 1)


cv2.waitKey()
cv2.destroyAllWindows()