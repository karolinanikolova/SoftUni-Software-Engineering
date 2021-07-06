# 2.	Words Lengths
# Using a list comprehension, write a program that receives some text, separated by comma and space ", ",
# and prints on the console each string with its length in the following format:
# "{first_str} -> {first_str_len}, {second_str} -> {second_str_len},…"

print(', '.join([f"{word} -> {len(word)}" for word in input().split(', ')]))
