def new_string(input_string):

    length = len(input_string)


    if length < 3:
        return "The input string must have at least 3 characters."


    elif length == 3:
        return input_string


    else:
        return input_string[0] + input_string[length // 2] + input_string[-1]


print(new_string("abc"))
print(new_string("abcd"))
print(new_string("abcdefghij"))
print(new_string("abc"))
print(new_string("ab"))