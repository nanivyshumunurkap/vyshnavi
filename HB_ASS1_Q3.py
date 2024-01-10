"""
 Write a program to remove characters from a string
starting from zero up to n and return a new string.
"""

def remove_chars(s, n):
    return s[n:]

s = "Hello, Satish!"
n = 7
new_string = remove_chars(s, n)
print(new_string)