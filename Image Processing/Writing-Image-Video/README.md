## Writing-Image-Video

### Writing Images using OpenCV
- OpenCV's imwrite() function can be used to write images to a specified location.

    **Syntax:** 
    cv2.imwrite(filename, image)

    **Parameters:**
    
    filename: A string representing the file name. The filename must include image format like .jpg, .png, etc.
    image: It is the image that is to be saved.

    **Return Value:** 
    It returns true if image is saved successfully.

    For more details, please refer to the associated Python script `write_image_opencv.py`.

### Writing Images using Pillow
- Pillow's save() function can be used to write images to a specified location.

    **Syntax:** 
    Image.save(fp, format=None, **params)

    **Parameters:**
    
    fp – A filename (string), pathlib.Path object or file object.
    format – Optional format override. If omitted, the format to use is determined from the filename extension. If a file object was used instead of a filename, this parameter should always be used.
    options – Extra parameters to the image writer.

    **Return Value:** 
    None

    For more details, please refer to the associated Python script `write_image_pil.py`