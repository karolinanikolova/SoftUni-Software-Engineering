# 03. Numbers
# Write a program to read a sequence of integers and find and print the top 5 numbers that are greater than
# the average value in the sequence, sorted in descending order.

sequence = [int(el) for el in input().split()]

average_value = sum(sequence) / len(sequence)

sequence.sort(reverse=True)

numbers_with_property = []

for number in sequence:
    if number > average_value:
        numbers_with_property.append(number)

    numbers_with_property = numbers_with_property[:5]

numbers_with_property = [str(el) for el in numbers_with_property]

if not numbers_with_property:
    print("No")
else:
    print(" ".join(numbers_with_property))

