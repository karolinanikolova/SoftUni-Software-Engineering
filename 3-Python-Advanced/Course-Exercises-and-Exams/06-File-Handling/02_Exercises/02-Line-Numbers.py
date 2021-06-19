# 2.	Line Numbers
# Write a program that reads a text file and inserts line numbers in front of each of its lines
# and counts all the letters and punctuation marks. The result should be written to another text file.

import re

with open("text.txt") as file:
    lines = [line.strip() for line in file.readlines()]

output = []

for index, line in enumerate(lines):
    character_count = sum([len(word) for word in line.split()])
    punctuation_count = sum([1 for word in line.split() for character in word if character in r'-,.!?\''])

    output.append(f'Line {index + 1}: {line} ({character_count - punctuation_count})({punctuation_count})')

with open('output.txt', 'a') as output_file:
    output_file.writelines([line + '\n' for line in output])
