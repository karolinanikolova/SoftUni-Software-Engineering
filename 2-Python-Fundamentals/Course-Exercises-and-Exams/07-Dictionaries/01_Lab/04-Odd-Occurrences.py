# 4.	Odd Occurrences
# Write a program that extracts all elements from a given sequence of words that are present in it an odd number of times (case-insensitive).
# •	Words are given on a single line, space separated.
# •	Print the result elements in lowercase, in their order of appearance.

words = input().split()

dict = {}

for word in words:
    word_lower = word.lower()
    if word_lower not in dict:
        dict[word_lower] = 0
    dict[word_lower] += 1

for word, count_present in dict.items():
    if not count_present % 2 == 0:
        print(word, end=" ")
