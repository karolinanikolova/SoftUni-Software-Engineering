# Character Multiplier
# Create a program that receives two strings on a single lines separated by space and prints the sum of their character
# codes multiplied (multiply str1[0] with str2[0] and add to the total sum). Then continue with the next two characters.
# If one of the strings is longer than the other, add the remaining character codes to the total sum without multiplication.

str1, str2 = input().split()

min_length = min(len(str1), len(str2))

total_sum = 0
remaining_characters = None

for index in range(min_length):
    total_sum += ord((str1[index])) * ord(str2[index])

if len(str1) > min_length:
    remaining_characters = str1[min_length:len(str1)]

if len(str2) > min_length:
    remaining_characters = str2[min_length:len(str2)]

if remaining_characters:
    for character in remaining_characters:
        total_sum += ord(character)

print(total_sum)
