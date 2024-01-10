"""
Write a program to accept a string from the user and
display characters that are present at an even index
number
"""
string = input("Enter any name: ")

print("even index from entered name: ", end="")
for i in range(0, len(string), 2):
    print(string[i], end="")
print()