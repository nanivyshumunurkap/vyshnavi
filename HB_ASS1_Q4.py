"""
 Write a function to return Ture if the first and last number
of a given list is same. If numbers are different then return
False.

"""

def first_and_last (numbers):

    if not numbers:
        return False

    return numbers[0] == numbers[-1]


my_list = [1, 2, 3, 4, 1]
result = first_and_last(my_list)
print(result)