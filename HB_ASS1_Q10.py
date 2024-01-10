def count_substring(input_string, substring):
    count = input_string.count(substring)
    return count

print(count_substring("Rahul is a doctor.", "doctor"))
print(count_substring("a quick brown fox.", "brown"))
print(count_substring("123-456-789", "-"))
print(count_substring("Hello, world!", "greetings"))