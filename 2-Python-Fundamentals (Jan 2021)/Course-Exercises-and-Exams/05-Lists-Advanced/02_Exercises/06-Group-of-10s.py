# 6.	Group of 10's
# Write a program that receives a list of numbers (string containing integers separated by ", ")
# and prints lists with the numbers them into lists of 10's.
# Examples:
# •	The numbers 2 8 4 3 fall into the group under 10
# •	The numbers 13 19 14 15 fall into the group under 20
# For more details, see the examples below

numbers = [int(el) for el in input().split(", ")]

# numbers = list(map(int, input().split(", ")))
# numbers = list(map(lambda x: int(x), input().split(", ")))

group = 10
max_number = max(numbers)

while numbers:
    numbers_group = []

    for num in numbers:
        if num in range(group-10, group+1):
            numbers_group.append(num)

    for num in numbers_group:
        numbers.remove(num)

    print(f"Group of {group}'s: {numbers_group}")

    group += 10
