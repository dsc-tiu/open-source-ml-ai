#This Python script shows how to write/save a video using OpenCV's VideoWriter() function.

#Import the necessary libraries
import os
import cv2

#If you are not familiar with reading videos using OpenCV, please refer to the 'Reading-Image-Video' folder.
video = cv2.VideoCapture(0)

if (video.isOpened() == False): 
    print("Error reading video file")

frame_width = int(video.get(3))
frame_height = int(video.get(4))
size = (frame_width, frame_height)

#For the various extensions supported by cv2.VideoWriter_fourcc, please refer to https://learn.microsoft.com/en-us/windows/win32/medfound/video-fourccs
result = cv2.VideoWriter('assets/webcam_save.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 10, size)
    
while True:
    _, frame = video.read()
    result.write(frame)
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


#Clean-up
video.release()
result.release()
cv2.destroyAllWindows()
