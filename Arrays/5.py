# 5. Write a Python program to get the current memory address and the length in elements of the buffer used to hold an array's contents. Also, find the size of the memory buffer in bytes.

# Importing numpy s np
import numpy as np

# Defining a numpy list
array = np.array([1, 3, 5, 7, 9])

# Getting the memory adress of the list with id()
memory_address_list = id(array)

# Getting the length of the list
array_length = len(array)

# Getting the list buffer size
array_buffer = array.nbytes

# Printing it in a fancier way
print(f"Information about the array:\nMemory Address List: {memory_address_list} \nLength of Array: {array_length} \nSize of Array Buffer: {array_buffer}")
