#This Python script shows how to read a video using OpenCV

#Import the necessary libraries
import cv2

#Initialize the VideoCapture object
cap = cv2.VideoCapture('assets/video.mp4')

# Check if camera opened successfully
if (cap.isOpened()== False):
  print("Error opening video")

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        # Display the resulting frame
        cv2.imshow('Video',frame)
        # Press Q on keyboard to exit (or) move to the next frame after 1 milliseconds
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# When everything done, release the video capture object and close all opened windows
cap.release()
cv2.destroyAllWindows()

