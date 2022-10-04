# Median Filter implementation
is a nonlinear operation often used in image processing to reduce "salt and pepper" noise. The `Median_Filter_implementation.py` method code takes 2 parameter arguments, the image array value and the image filter size.
Lets say you have your Image array data in a variable called data, and you want to remove this noise from your image using a 3x3 median filter. This is the function to do it

```
img_median = median_filter(data, 3) 
```

For a 5x5 median filter, you only need to change the second parameter argument to 5.

# Experiment

###### This image is noisy image -corrupted by salt and pepper noise. We will run the code and try to remove the noise from the image.

<p align="center"><img src=" "/></p>

###### This is the result after running your code with using 3x3 median filter.

<p align="center"><img src=" "/></p>





