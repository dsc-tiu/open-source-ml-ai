## Writing-Image-Video

### Writing Images using OpenCV
- OpenCV's imwrite() function can be used to write images to a specified Location

    **Syntax:** 
    cv2.imwrite(filename, image)

    **Parameters:**
    filename: A string representing the file name. The filename must include image format like .jpg, .png, etc.
    image: It is the image that is to be saved.

    **Return Value:** 
    It returns true if image is saved successfully.

    For more details, please refer to the associated Python script `write_image_opencv.py`