# 2.	Repeat Strings
# Write a Program That Reads a list of strings. Each string is repeated N times, where N is the length of the string. Print the concatenated string.

strings = input().split()

output_string = ""

for string in strings:
    N = len(string)

    output_string += string * N

print(output_string)
