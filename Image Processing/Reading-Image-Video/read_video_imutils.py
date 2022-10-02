#This Python script shows how to use the imutils library to speed up frame reading

#Import the necessary libraries
import cv2
import time
from imutils.video import WebcamVideoStream


#Initialize the WebcamVideoStream object; src=0 refers to the webcam
vs = WebcamVideoStream(src=0).start()

while True:
    imutils_frame= vs.read()
    
    cv2.imshow("IMUTILS",imutils_frame)
    key = cv2.waitKey(1) 
    if key == 27: #esc key stops the process
        break


## When everything done, release the object and close all opened windows
vs.stop()    
cv2.destroyAllWindows()    
