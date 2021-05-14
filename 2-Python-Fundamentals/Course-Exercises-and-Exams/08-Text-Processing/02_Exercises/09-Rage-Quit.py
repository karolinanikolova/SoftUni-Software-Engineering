# 9.	 *Rage Quit
# Every gamer knows what rage-quitting means. It’s basically when you’re just not good enough and you blame everybody
# else for losing a game. You press the CAPS LOCK key on the keyboard and flood the chat with gibberish to show your frustration.
# Chochko is a gamer, and a bad one at that. He asks for your help; he wants to be the most annoying kid in his team,
# so when he rage-quits he wants something truly spectacular. He’ll give you a series of strings followed
# by non-negative numbers, e.g. "a3"; you need to print on the console each string repeated N times;
# convert the letters to uppercase beforehand. In the example, you need to write back "AAA".
# On the output, print first a statistic of the number of unique symbols used (the casing of letters is irrelevant,
# meaning that 'a' and 'A' are the same); the format shoud be "Unique symbols used {0}". Then, print the rage message itself.
# The strings and numbers will not be separated by anything.
# The input will always start with a string and for each string there will be a corresponding number.
# The entire input will be given on a single line; Chochko is too lazy to make your job easier.

# input_string = input()
#
# start_index = 0
#
# strings = []
# numbers = []
# is_previous_char_digit = False
#
# output_string = ''
#
# for index in range(len(input_string)):
#
#     if is_previous_char_digit:
#         is_previous_char_digit = False
#         continue
#
#     if input_string[index].isdigit():
#
#         end_index = index
#         strings.append(input_string[start_index:end_index])
#
#         if index < len(input_string) - 1:
#             if input_string[index+1].isdigit():
#                 is_previous_char_digit = True
#                 numbers.append(input_string[index:index+2])
#                 start_index = end_index + 2
#             else:
#                 numbers.append(input_string[index])
#                 start_index = end_index + 1
#         else:
#             numbers.append(input_string[index])
#             start_index = end_index + 1
#
# for index in range(len(strings)):
#     output_string += int(numbers[index]) * strings[index].upper()
#
# print(f"Unique symbols used: {len(set(output_string))}")
# print(output_string)

input_string = input()

index = 0
current_string = ""
final_result = ""

while index < len(input_string):

    if not input_string[index].isdigit():
        current_string += input_string[index]
        index += 1
    else:
        current_number = ""
        while input_string[index].isdigit():
            current_number += input_string[index]
            index += 1
            if index == len(input_string):
                break
        current_number = int(current_number)
        output_string = current_string.upper() * current_number
        final_result += output_string
        current_string = ""

print(f"Unique symbols used: {len(set(final_result))}")
print(final_result)






