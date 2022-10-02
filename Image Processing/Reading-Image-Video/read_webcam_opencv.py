#This Python script shows how to read a video using OpenCV

#Import the necessary libraries
import cv2

#Initialize the VideoCapture object
cap = cv2.VideoCapture(0)

# Check if camera opened successfully
if (cap.isOpened()== False):
  print("Error opening video")

while True:
    _, frame = cap.read()
    cv2.imshow('Video',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the video capture object and close all opened windows
cap.release()
cv2.destroyAllWindows()

