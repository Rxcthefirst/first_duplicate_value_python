# Algorithm practice
#
# Description: Create a function that takes in an array of integers between 1 and n, where n
# is the length of the array, and returns the first integers that appears more than once
# when the array is read from left to right. If no integer appears more than once, return -1.

def first_duplicate_value(array):
    # Initialize an empty array.
    numbers_used = set()

    for value in array:
        if value in numbers_used:
            return value
        numbers_used.add(value)

    return -1


print(first_duplicate_value([1, 2, 3, 4, 5, 3, 4, 1]))
