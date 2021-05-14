# 4. Odd and Even Sum
# You will receive a single number. You have to write a function that returns the sum of all even and all odd digits
# from that number as a single string like in the examples below.

def get_odd_and_even_sum(num_as_string):
    odd_sum = 0
    even_sum = 0

    for char in num_as_string:
        current_char_as_num = int(char)

        if current_char_as_num % 2 == 0:
            even_sum += current_char_as_num
        else:
            odd_sum += current_char_as_num

    return [odd_sum, even_sum]


number_as_string = input()

result = get_odd_and_even_sum(number_as_string)

print(f'Odd sum = {result[0]}, Even sum = {result[1]}')

# # With list
# def get_odd_and_even_sum(num_as_string):
#     num_list = list(map(int, num_as_string))
#     odd_sum = 0
#     even_sum = 0
#
#     for element in range(len(num_list)):
#         if num_list[element] % 2 == 0:
#             even_sum += num_list[element]
#         else:
#             odd_sum += num_list[element]
#
#     return [odd_sum, even_sum]
#
#
# number_as_string = input()
#
# result = get_odd_and_even_sum(number_as_string)
#
# print(f'Odd sum = {result[0]}, Even sum = {result[1]}')