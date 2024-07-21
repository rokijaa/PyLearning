# 6. Write a Python program to get the number of occurrences of a specified element in an array.

# defining an array/list
array = [1,3,5,3,7,9,3]
# count var for the number
number_count = 0

# for x in the range of length of array we check if the current list item is 3 if yes, then number count +1
for x in range(len(array)):
    if array[x] == 3:
        number_count += 1
print(f"Number of occurrences of the number 3 in the said array: {number_count}")