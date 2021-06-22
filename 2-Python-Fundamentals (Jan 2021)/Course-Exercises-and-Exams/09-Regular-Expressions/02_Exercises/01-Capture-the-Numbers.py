# 1.	Capture the Numbers
# Write a program that finds all numbers in a sequence of strings.
# The output is all the numbers, extracted and printed on a single line – each separated by a single space.

import re

text_line = input()
pattern = r"\d+"

all_numbers = []

# while not text_line == "":
while text_line:
    numbers = re.findall(pattern, text_line)

    all_numbers.extend(numbers)

    text_line = input()

# print(" ".join(all_numbers))
print(*all_numbers)