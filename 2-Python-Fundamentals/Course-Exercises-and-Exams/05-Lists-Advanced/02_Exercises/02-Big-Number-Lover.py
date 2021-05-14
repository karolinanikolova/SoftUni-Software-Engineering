# 2.	Big Numbers Lover
# You really like big numbers, so you always find a way to form one from numbers given to you
# You will receive a single line containing numbers separated by a single space.
# Sort and reverse the numbers then return them as a string.

numbers_as_string = input().split()
numbers_as_string_descending = sorted(numbers_as_string, reverse=True)

print("".join(numbers_as_string_descending))
