# 5.	Balanced Brackets
# You will receive n lines. On those lines, you will receive one of the following:
# •	Opening bracket – “(“,
# •	Closing bracket – “)” or
# •	Random string
# Your task is to find out if the brackets are balanced. That means after every closing bracket should follow an opening one.
# Nested parentheses are not valid, and if two consecutive opening brackets exist, the expression should be marked as unbalanced.

number_of_lines = int(input())

is_last_opening = False
is_last_closing = False
is_balanced = True

for line in range(1, number_of_lines + 1):
    character = input()
    if len(character) > 1:
        continue
    if is_last_opening and ord(character) == 40:
        is_balanced = False
    if is_last_closing and ord(character) == 41:
        is_balanced = False

    is_last_opening = False
    is_last_closing = False

    if ord(character) == 40:
        is_last_opening = True
    if ord(character) == 41:
        is_last_closing = True

if is_balanced:
    print('BALANCED')
else:
    print('UNBALANCED')