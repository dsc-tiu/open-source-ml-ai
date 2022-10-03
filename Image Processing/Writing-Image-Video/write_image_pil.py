#This Python script shows how to write an image using PIL's save() function.

#Import the necessary libraries
import os
from PIL import Image 

#Initialize path variables
input_path = "assets/python_logo.png"
output_path = "assets/python_logo_save.png"

#Display the image 
#If you are not familar with reading images using PIL, please refer to the 'Reading-Image-Video' folder.
img = Image.open(input_path)
img.show()

#Write the image to the 'assets' folder
img.save(output_path)