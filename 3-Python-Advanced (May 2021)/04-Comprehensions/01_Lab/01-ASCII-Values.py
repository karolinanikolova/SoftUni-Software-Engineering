# 1.	ASCII Values
# Write program that receives a list of characters separated by ", " and creates a dictionary with each character
# as a key and its ASCII value as a value. Try solving that problem using comprehensions.

dictionary = {ch: ord(ch) for ch in input().split(', ')}

print(dictionary)