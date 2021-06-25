# 5.	Odd or Even
# On the first line you will receive a command - "Odd" or "Even". On the second line you will receive a sequence of
# numbers (integers), separated by a single space.
# •	If the command is "Odd", print the sum of the Odd numbers multiplied by the count of all numbers.
# •	If the command is "Even", print the sum of the Even numbers multiplied by the count of all numbers.

def odd_or_even(com, nums):
    if com == "Odd":
        filtered_nums = list(filter(lambda x: x % 2 != 0, nums))
    elif com == "Even":
        filtered_nums = list(filter(lambda x: x % 2 == 0, nums))

    return sum(filtered_nums) * len(nums)


command = input()
numbers = [int(el) for el in input().split()]

print(odd_or_even(command, numbers))
