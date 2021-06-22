# 3.	Find Occurrences of Word in Sentence
# Write a program that finds, how many times a given word, is used in a given sentence.
# Note that letter case does not matter – it is case-insensitive.
# The output is a single number indicating the amount of times the sentence contains the word.

import re

text = input()

searched_text = input()

pattern = rf"\b{searched_text}\b"

print(len(re.findall(pattern, text, re.IGNORECASE)))
