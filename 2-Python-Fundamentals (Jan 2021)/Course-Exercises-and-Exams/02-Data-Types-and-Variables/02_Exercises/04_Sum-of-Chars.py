# 4.	Sum of Chars
# Write a program, which sums the ASCII codes of n characters and prints the sum on the console.
# Input
# •	On the first line, you will receive n – the number of lines, which will follow
# •	On the next n lines – you will receive letters from the Latin alphabet
# Output
# Print the total sum in the following format:
# The sum equals: {total_sum}

number_of_characters = int(input())
total_sum = 0

for _ in range(1, number_of_characters + 1):
    character = input()
    character_ASCII = ord(character)
    total_sum += character_ASCII

print(f'The sum equals: {total_sum}')