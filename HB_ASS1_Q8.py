def count_chars(input_string):
    char_count = {}
    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

print(count_chars("abcabc"))
print(count_chars("abcd"))
print(count_chars("abccba"))
print(count_chars(""))