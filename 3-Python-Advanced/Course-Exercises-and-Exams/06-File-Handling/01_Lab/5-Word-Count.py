# 5.	Word Count
# Write a program that reads a list of words from the file words.txt and finds how many times each
# of the words is contained in another file text.txt. Matching should be case-insensitive.
# The results should be written to another text files. Sort the words by frequency in descending order.

import re

with open("words.txt", "w") as file:
    file.write('quick is fault')

with open("input.txt", "w") as file:
    file.write("-I was quick to judge him, but it wasn't his fault.\n")
    file.write("-Is this some kind of joke?! Is it?\n")
    file.write("-Quick, hide here...It is safer.\n")

with open("words.txt") as file:
    searched_words = file.read().split()

occurrences= {}

with open("input.txt") as file:
    content = file.read().lower()
    for s_word in searched_words:
        result = re.findall(rf"(?<=(\-|\s)){s_word}(?=(\.|))", content)
        occurrences[s_word] = len(result)

sorted_result = sorted(occurrences.items(), key=lambda x: -x[1])

for key, value in sorted_result:
    print(f"{key} - {value}")