# # Without queue
#
# numbers = [int(el) for el in input().split(',')]
# target_index = int(input())
# target_number = numbers[target_index]
#
# count_clock_cycles = 0
#
# for number in numbers:
#     if number < target_number:
#         count_clock_cycles += number
#
# for number in numbers[:target_index]:
#     if number == target_number:
#         count_clock_cycles += number
#
# count_clock_cycles += target_number
#
#
# print(count_clock_cycles)

# With queue

from collections import deque

numbers = deque([int(el) for el in input().split(',')])
target_index = int(input())
target_number = numbers[target_index]

count_clock_cycles = 0

for index in range(0, target_index):
    if numbers[index] == target_number:
        count_clock_cycles += numbers[index]

while min(numbers) < target_number:
    count_clock_cycles += min(numbers)
    numbers.remove(min(numbers))

count_clock_cycles += target_number

print(count_clock_cycles)