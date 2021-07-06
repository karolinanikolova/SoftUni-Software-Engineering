# 7.	Flatten Lists
# Write a program to flatten several lists of numbers, received in the following format:
# 	String with numbers or empty strings separated by '|'.
# 	Values are separated by spaces (' ', one or several)
# 	Order the output list from the last to the first received, and their values from left to right as shown below.

result = [string.split() for string in input().split('|')][::-1]

flatten_result = [el for sublist in result for el in sublist]

print(*flatten_result)