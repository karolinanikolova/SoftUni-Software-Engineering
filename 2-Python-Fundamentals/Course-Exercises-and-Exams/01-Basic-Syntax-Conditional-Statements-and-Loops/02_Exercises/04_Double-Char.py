# 4.	Double Char
# Given a string, you have to print a string in which each character (case-sensitive) is repeated.

text = input()

# for char in text:
#     print(char * 2, end='')


result_text = ''

for char in text:
    result_text += 2 * char

print(result_text)
