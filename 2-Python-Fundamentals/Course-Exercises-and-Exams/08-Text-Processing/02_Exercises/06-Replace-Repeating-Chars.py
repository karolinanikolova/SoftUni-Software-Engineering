# 6.	 Replace Repeating Chars
# Write a program that reads a string from the console and replaces any sequence of the same letters with a single corresponding letter.

string = input()

index = 0

while index < len(string) - 1:
    if string[index] == string[index + 1]:
        element_to_replace = f"{string[index]}{string[index + 1]}"
        string = string.replace(element_to_replace, string[index])
        index = 0
    else:
        index += 1

print(string)
