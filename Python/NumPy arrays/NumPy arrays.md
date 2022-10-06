# **NumPy Arrays**

## About
Numpy is a core library used in Data Science, and an array is its most central data structure. NumPy aims to provide an array object that is up to 50x faster than traditional Python lists. This multidimensional array object has incredible speed, and the library also provides various tools to interact with these arrays. <br/>
We will go over these tools in different Python programs.
## NumPy Array
Firstly, what is an array? </br> 
Where an element is found, how to interpret an element and all this information about the raw data is found in an *array*, which is a grid of values. 
This grid can be indexed in different ways. The elements are all of the same type, referred to as the *array dtype*.<br/>
An N-dimensional array is simply an array with any number of dimensions.
## Code explanation
The Python programs describe the basic functions of the NumPy array through the following sub topics:

1. Attributes of arrays: <br/>
To determine the size, dimension, memory consumption, and data types of arrays.
2. Indexing of arrays:<br/> To get and assign value of individual array elements.
3. Slicing of arrays:<br/> To get and to insert or set smaller subarrays within a larger array.
4. Reshaping of arrays:<br/> To change the shape of a given array.
5. Joining and splitting of arrays:<br/>To combine multiple arrays into one, and to split one array into many.

## NumPy array vs Python list
### Differences

The use of an NumPy array saves memory and is simple. NumPy offers a means for specifying the data types and utilises significantly less RAM to store data. This enables even more code optimization.

Elements of an array are stored contiguously in memory. For example, all rows of a two-dimensioned array must have the same number of columns. In a Python list, the elements do not have to be in contiguous memory.

Another major difference is that unlike Python lists, NumPy arrays have a fixed type. For example, if a floating-point value is added to an integer array, the value will be silently truncated.

### Advantages of NumPy arrays
1. Consumes lesser memory.
2. Fast as compared to the Python List.
3. Element-wise operation is possible in NumPy arrays unlike in Python lists.
3. Convenient to use.



