# 4. Write a Python program to get the length in bytes of one array item in the internal representation.

import numpy as np

# Create an numpy array 
my_array = np.array([1, 2, 3, 4, 5])

# Get the size of each item in the numpy array
item_size = my_array.itemsize

# Print the itemsize of each item in a fancy way
print(f"Size of each item in the numpy array: {item_size} bytes")