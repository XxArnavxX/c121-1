import cv2
import time
import numpy as np

#To save the output
fourcc = cv2.VideoWriter_fourcc(*'XVID')
outputfile = cv2.VideoWriter('output.avi', fourcc, 30.0, (640, 480))

#To start the webcam
cam = cv2.VideoCapture(0)

#make the code sleep
time.sleep(5)

#making it loop 60 seconds
for i in range(60):
    ret, bg = cam.read()

bg = np.flip(bg, axis = 1)

#capturing then flipping
while(cam.isOpened()):
    ret, ing = cam.read()
    if not ret:
        break