data_integer = 1112132131231232
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
print("- Type : ", type(data_c_double))