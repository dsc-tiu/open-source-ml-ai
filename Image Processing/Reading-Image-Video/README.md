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

### Reading videos using OpenCV
- A video is simply a sequence of frames.
- OpenCV provides functions for reading video streams as a sequence of frames.
- OpenCV's video reading methods are widely used.

1. Reading a video using OpenCV
    **Syntax - I:** cv2.VideoCapture(path)
    **Parameters:**
    path: A string representing the path of the image to be read.
    **Return Value:** This method returns a VideoCapture object that can be used to read the file.

    **Syntax - II:** <<VideoCapture object>>.read()
    **Parameters:**
    path: A string representing the path of the image to be read.
    **Return Value:** This method returns two values:
    1. ret - a flag indicating if the last frame has been read. This value is always false till the last frame.
    2. frame - frame of a video

    For more implementation details, please refer to the associated Python script: `read_video_opencv.py`.
