## Reading-Image-Video

### Reading an image using OpenCV
- Images can be read using OpenCV's imread() function. 

    **Syntax:** cv2.imread(path, flag)
    **Parameters:**
    path: A string representing the path of the image to be read.
    flag: It specifies the way in which image should be read. It’s default value is cv2.IMREAD_COLOR

    **Return Value:** This method returns an image object that is loaded from the specified file.

    For more implementation details, please refer to the associated Python notebook: `read_image_opencv.ipynb`.

### Reading an image using PIL
- Images can also be read using the Pillow's Image() function.
    **Syntax:** PIL.Image(path,mode="r")
    **Parameters:**
    path: A string representing the path of the image to be read.
    mode – The mode. If given, this argument must be “r”. Hence, this parameter is superfluous.

    **Return Value:** This method returns an image object that is loaded from the specified file.

    For more implementation details, please refer to the associated Python notebook: `read_image_pil.ipynb`.
