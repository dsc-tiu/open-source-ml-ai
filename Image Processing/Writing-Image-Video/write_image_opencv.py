#This Python script shows how to write an image using OpenCV's imwrite() function.

#Import the necessary libraries
import os
import cv2

#Initialize path variables
input_path = "assets/python_logo.png"
output_path = "assets/python_logo_save.png"

#Display the image 
#If you are not familar with reading images using OpenCV, please refer to the 'Reading-Image-Video' folder.
img = cv2.imread(input_path)
cv2.imshow("Image",img)

#wait till user presses a key
cv2.waitKey(0)

#Write the image to the 'assets' folder
cv2.imwrite(output_path,img)
