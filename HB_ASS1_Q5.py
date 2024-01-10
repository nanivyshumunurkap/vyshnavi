
"""
 Write a function to return Ture if the first and last number
of a given list is same. If numbers are different then return
False.

"""

def merge_lists(lst1, lst2):

    new_list = []


    for num in lst1:
        if num % 2 != 0:
            new_list.append(num)


    for num in lst2:
        if num % 2 == 0:
            new_list.append(num)

    return new_list

lst1 = [1, 2, 3, 4, 5]
lst2 = [6, 7, 8, 9, 10]

new_list = merge_lists(lst1, lst2)
print(new_list)