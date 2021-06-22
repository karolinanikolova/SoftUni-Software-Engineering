# 1.	Count Chars in a String
# Write a program that counts all characters in a string except for space (' ').
# Print all the occurrences in the following format:
# {char} -> {occurrences}

string = input()

dictionary = {}

for character in string:
    if character == ' ':
        continue
    if character not in dictionary:
        dictionary[character] = 0
    dictionary[character] += 1

for char, occurrences in dictionary.items():
    print(f"{char} -> {occurrences}")
