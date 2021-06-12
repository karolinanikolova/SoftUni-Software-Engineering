# 1.	Count Same Values
# You will be given numbers separated by a space. Write a program which prints the number of occurrences of each number
# in the format "{number} - {count} times".

numbers = tuple([int(el) for el in input().split()])

result = {}

for el in numbers:
    if el not in result:
        result[el] = 1
    else:
        result[el] += 1

# for key, value in result.items():
#     print(f"{key:.1f} - {value} times")

[print(f"{key:.1f} - {value} times") for key, value in result.items()]
