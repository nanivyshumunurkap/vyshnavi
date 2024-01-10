"""
wite a program to iterate the first 10 numbers, and in
each iteration, print the sum of the current and previous
number
"""

for i in range(1, 11):
    start_num = i
    prev_num = i - 1
    sum_of_num = start_num + prev_num
    print(f"Starting number: {start_num}, Previous number: {prev_num}, Sum: {sum_of_num}")
