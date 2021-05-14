# 5.	Digits, Letters and Other
# Write a program that receives a single string and on the first line prints all the digits,
# on the second – all the letters, and on the third – all the other characters.
# There will always be at least one digit, one letter and one other characters.

# string = input()
#
# digits = ""
# letters = ""
# other = ""
#
# for character in string:
#     if character.isdigit():
#         digits += character
#     elif character.isalpha():
#         letters += character
#     else:
#         other += character
#
# print(digits)
# print(letters)
# print(other)

string = input()
separator = "\n"
print(separator.join([''.join(filter(lambda x: x.isdigit(), string)),
                     ''.join(filter(lambda x: x.isalpha(), string)),
                     ''.join(filter(lambda x: not x.isalpha() and not x.isdigit(), string))]))
