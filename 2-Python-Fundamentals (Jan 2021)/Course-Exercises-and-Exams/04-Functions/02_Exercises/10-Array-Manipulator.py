# 10. *Array Manipulator
# Trifon has finally become a junior developer and has received his first task. It's about manipulating an array of integers. He is not quite happy about it, since he hates manipulating arrays. They are going to pay him a lot of money, though, and he is willing to give somebody half of it if to help him do his job. You, on the other hand, love arrays (and money) so you decide to try your luck.
# The array may be manipulated by one of the following commands
# •	exchange {index} – splits the array after the given index, and exchanges the places of the two resulting sub-arrays. E.g. [1, 2, 3, 4, 5] -> exchange 2 -> result: [4, 5, 1, 2, 3]
# o	If the index is outside the boundaries of the array, print "Invalid index"
# •	max even/odd– returns the INDEX of the max even/odd element -> [1, 4, 8, 2, 3] -> max odd -> print 4
# •	min even/odd – returns the INDEX of the min even/odd element -> [1, 4, 8, 2, 3] -> min even > print 3
# o	If there are two or more equal min/max elements, return the index of the rightmost one
# o	If a min/max even/odd element cannot be found, print "No matches"
# •	first {count} even/odd– returns the first {count} elements -> [1, 8, 2, 3] -> first 2 even -> print [8, 2]
# •	last {count} even/odd – returns the last {count} elements -> [1, 8, 2, 3] -> last 2 odd -> print [1, 3]
# o	If the count is greater than the array length, print "Invalid count"
# o	If there are not enough elements to satisfy the count, print as many as you can. If there are zero even/odd elements, print an empty array "[]"
# •	end – stop taking input and print the final state of the array
# Input
# •	The input data should be read from the console.
# •	On the first line, the initial array is received as a line of integers, separated by a single space
# •	On the next lines, until the command "end" is received, you will receive the array manipulation commands
# •	The input data will always be valid and in the format described. There is no need to check it explicitly.
# Output
# •	The output should be printed on the console.
# •	On a separate line, print the output of the corresponding command
# •	On the last line, print the final array in square brackets with its elements separated by a comma and a space
# •	See the examples below to get a better understanding of your task
# Constraints
# •	The number of input lines will be in the range [2 … 50].
# •	The array elements will be integers in the range [0 … 1000].
# •	The number of elements will be in the range [1 .. 50]
# •	The split index will be an integer in the range [-231 … 231 – 1]
# •	first/last count will be an integer in the range [1 … 231 – 1]
# •	There will not be redundant whitespace anywhere in the input
# •	Allowed working time for your program: 0.1 seconds. Allowed memory: 16 MB.

def exchange(nums_list, index):
    result = nums_list
    if index > len(nums_list) or index <= 0:
        print("Invalid index")
    else:
        array_output1 = nums_list[index+1::]
        array_output2 = nums_list[:index+1]
        result = array_output1 + array_output2
    return result


def find_max_num(nums_list, odd_or_even_command):
    filtered_nums = []
    if odd_or_even_command == 'odd':
        for el in nums_list:
            if not el % 2 == 0:
                filtered_nums.append(el)
    else:
        for el in nums_list:
            if el % 2 == 0:
                filtered_nums.append(el)

    if not filtered_nums: # if list is empty
        return 'No matches'

    max_element = max(filtered_nums)
    index = len(nums_list) - nums_list[::-1].index(max_element) - 1

    return index


def find_min_num(nums_list, odd_or_even_command):
    filtered_nums = []
    if odd_or_even_command == 'odd':
        for el in nums_list:
            if not el % 2 == 0:
                filtered_nums.append(el)
    else:
        for el in nums_list:
            if el % 2 == 0:
                filtered_nums.append(el)

    if not filtered_nums: # if list is empty
        return 'No matches'

    min_element = min(filtered_nums)
    index = len(nums_list) - nums_list[::-1].index(min_element) - 1

    return index


def find_first(nums_list, count, odd_or_even_command):
    filtered_nums = []
    if odd_or_even_command == 'odd':
        for el in nums_list:
            if not el % 2 == 0:
                filtered_nums.append(el)
    else:
        for el in nums_list:
            if el % 2 == 0:
                filtered_nums.append(el)

    if len(nums_list) < count:
        return 'Invalid count'

    return filtered_nums[:count]


def find_last(nums_list, count, odd_or_even_command):
    filtered_nums = []
    if odd_or_even_command == 'odd':
        for el in nums_list:
            if not el % 2 == 0:
                filtered_nums.append(el)
    else:
        for el in nums_list:
            if el % 2 == 0:
                filtered_nums.append(el)

    if len(nums_list) < count:
        return 'Invalid count'

    # Reverse list, then take the last two numbers, then reverse the result
    return filtered_nums[::-1][:count][::-1]


nums_as_string = input().split()
nums = []

for el in nums_as_string:
    nums.append(int(el))

command_data = input()

while command_data != 'end':

    command_data = command_data.split()
    command = command_data[0]

    if command == 'exchange':
        i = int(command_data[1])
        nums = exchange(nums, i)

    elif command == "max":
        odd_or_even = command_data[1]
        print(find_max_num(nums, odd_or_even))

    elif command == "min":
        odd_or_even = command_data[1]
        print(find_min_num(nums, odd_or_even))

    elif command == "first":
        odd_or_even = command_data[2]
        counter = int(command_data[1])
        print(find_first(nums, counter, odd_or_even))

    elif command == "last":
        odd_or_even = command_data[2]
        counter = int(command_data[1])
        print(find_last(nums, counter, odd_or_even))

    command_data = input()

print(nums)
