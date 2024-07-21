# 7. Write a Python program to append items from inerrable to the end of the array.

array = [1,3,5,7,9]

# We extend the original list/array with the array/list itself
array.extend(array)
print(array)