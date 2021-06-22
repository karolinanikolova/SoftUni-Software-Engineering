# 1.	Invert Values
# Write a program that receives a single string containing numbers separated by a single space.
# Print a list containing the opposite of each number.

string = input()

list = string.split(" ")

list_numbers = numbers = [int(x) for x in list]
myneglist = [-x for x in list_numbers]

print(myneglist)