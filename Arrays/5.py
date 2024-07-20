# 5. Write a Python program to get the current memory address and the length in elements of the buffer used to hold an array's contents. Also, find the size of the memory buffer in bytes.

# Defining python list
array = [1, 3, 5, 7, 9]

# Getting the memory adress of the list with id()
memory_adress_list = id(array)

# Getting the length of the list
array_length = len(array)

print(f"The memory address of the list is: {memory_adress_list}, and the lenght is: {array_length}")
