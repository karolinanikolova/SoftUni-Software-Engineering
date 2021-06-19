# 1.	Even Lines
# Write a program that reads a text file and prints on the console its even lines.
# Line numbers start from 0. Before you print the result replace {"-", ",", ".", "!", "?"}
# with "@" and reverse the order of the words.

import re

with open("text.txt") as file:
    lines = file.readlines()

for index, line in enumerate(lines):
    if not index % 2 == 0:
        continue

    line = re.sub('[-,.!?]', '@', line)
    line = ' '.join(reversed(line.split()))

    print(line)

