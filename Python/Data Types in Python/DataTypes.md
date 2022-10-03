# Python Data Types

DataTypes.py :
` data_integer = 1112132131231232
print("Value : ", data_integer)
print("- Type : ", type(data_integer))

data_float = 1.5
print("Value : ", data_float)
print("- Type : ", type(data_float))

data_string = "Maul"
print("Value : ", data_string)
print("- Type : ", type(data_string))

data_bool = False
print("Value : ", data_bool)
print("- Type : ", type(data_bool))

data_complex = complex(5,6)
print("Value : ", data_complex)
print("- Type : ", type(data_complex))

from ctypes import c_double, c_char

data_c_double = c_double(10.5)
print("Value : ", data_c_double)
print("- Type : ", type(data_c_double)) `

Output from DataTypes.py :

`Value :  1112132131231232
- Type :  <class 'int'>
Value :  1.5
- Type :  <class 'float'>
Value :  Maul
- Type :  <class 'str'>
Value :  False
- Type :  <class 'bool'>
Value :  (5+6j)
- Type :  <class 'complex'>
Value :  c_double(10.5)
- Type :  <class 'ctypes.c_double'>`

## Code Explanation
Data types are an important concept in the python programming language. In Python, each value has its own python data type.

The output generated on `DataTypes.py` is the value of the data type of each input value data python

### Integers
There is no maximum limit on the value of an integer. The integer can be of any length without any limitation which can go up to the maximum available memory of the system. 

### Floating Point Number
The difference between floating points and integers is decimal points. Floating point number can be represented as “1.0”, and integer can be represented as “1”. It is accurate up to 15 decimal places.

### String
Strings are arrays of bytes representing Unicode characters. Python does not have a character data type, a single character is simply a string with a length of 1. Square brackets can be used to access elements of the string.

### Boolean
Boolean type is one of Python’s built-in data types. It’s used to represent the truth value of an expression. Booleans represent one of two values: True or False.

#### Complex Number
`x + yj` is the written form of the complex number. Here y is the imaginary part and x is the real part.

### Ctypes in Python
ctypes is a foreign function library for Python. It provides C compatible data types, and allows calling functions in DLLs or shared libraries. It can be used to wrap these libraries in pure Python.