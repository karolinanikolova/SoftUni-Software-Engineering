# 1.	Match Full Name
# Write a program to match full names from a list of names and print them on the console.
# Writing the Regular Expression
# First, write a regular expression to match a valid full name, according to these conditions:
# •	A valid full name has the following characteristics:
# o	It consists of two words.
# o	Each word starts with a capital letter.
# o	After the first letter, it only contains lowercase letters afterwards.
# o	Each of the two words should be at least two letters long.
# o	The two words are separated by a single space.

import re

pattern = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"

text = input()
valid_names = re.findall(pattern, text)
print(" ".join(valid_names))

# names = input().split(", ")
#
# valid_names = []
#
# for name in names:
#     match = re.match(pattern, name)
#     if match:
#
# print(" ".join(valid_names))

