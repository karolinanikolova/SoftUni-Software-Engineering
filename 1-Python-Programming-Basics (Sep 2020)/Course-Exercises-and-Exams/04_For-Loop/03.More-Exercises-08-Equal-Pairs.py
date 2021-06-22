# 8.	Еднакви двойки
# Дадени са 2*n-на брой числа. Първото и второто формират двойка, третото и четвъртото също и т.н.
# Всяка двойка има стойност – сумата от съставящите я числа. Напишете програма, която проверява дали всички двойки имат
# еднаква стойност или печата максималната разлика между две последователни двойки. Ако всички двойки имат еднаква
# стойност, отпечатайте "Yes, value = {Value}" + стойността. В противен случай отпечатайте "No, maxdiff = {Difference}"
# + максималната разлика.

#  Solution method 1
import sys

n = int(input())
temp_sum = 0
max_diff = - sys.maxsize
sum_of_all_pairs = 0
is_equal = True

for i in range(1, n + 1):
    first_number_from_pair = int(input())
    second_number_from_pair = int(input())
    if i >= 2:
        if temp_sum == 0:
            diff = 0
        elif temp_sum == first_number_from_pair + second_number_from_pair:
            is_equal = True
        else:
            is_equal = False
            diff = abs(temp_sum - (first_number_from_pair + second_number_from_pair))
            if diff > max_diff:
                max_diff = diff
    temp_sum = first_number_from_pair + second_number_from_pair
    sum_of_all_pairs += temp_sum


if is_equal:
    print(f'Yes, value={int(sum_of_all_pairs / n)}')
else:
    print(f'No, maxdiff={max_diff}')



# #  Solution method 2 - with one input in the for loop (more complex)
# import sys
#
# n = int(input())
# temp_sum = 0
# sum = 0
# temp_number = 0
# max_diff = - sys.maxsize
# sum_of_all_pairs = 0
# is_equal = True
#
# for i in range(1, 2 * n + 1):
#     number = int(input())
#     if i % 2 == 0:
#         sum = number + temp_number
#     if i >= 4:
#         if temp_sum == number + temp_number:
#             is_equal = True
#         else:
#             is_equal = False
#             diff = abs(temp_sum - sum)
#             if diff > max_diff:
#                 max_diff = diff
#     temp_number = number
#     temp_sum = sum
#     sum_of_all_pairs += temp_number
#
# if is_equal:
#     print(f'Yes, value={int(sum_of_all_pairs / n)}')
# else:
#     print(f'No, maxdiff={max_diff}')




# # Solution method 3 - with lists (not studied so far)
# n = int(input())
# sum_pair_list = []
# diff = []
# if n == 1:
#     is_sum_pair_equal = True
# else:
#     is_sum_pair_equal = False
#
# for i in range(1, n + 1):
#     first_number_from_pair = int(input())
#     second_number_from_pair = int(input())
#     sum_pair = first_number_from_pair + second_number_from_pair
#     sum_pair_list.append(sum_pair)
#
# for i in range(1, n):
#     if sum_pair_list[i] == sum_pair_list[i-1]:
#         is_sum_pair_equal = True
#     else:
#         is_sum_pair_equal = False
#     diff.append(abs(sum_pair_list[i] - sum_pair_list[i - 1]))
#
# if is_sum_pair_equal:
#     print(f'Yes, value={sum_pair_list[0]}')
# else:
#     print(f'No, maxdiff={max(diff)}')


# # Lecturer solution
# n = int(input())
#
# is_all_equal = True
# current_sum = 0
# previous_sum = 0
# biggest_difference_between_two_couples = 0
#
# for numbers in range(1, 2 * n + 1):
#     number = int(input())
#     if numbers % 2 == 0:
#         current_sum += number
#         if numbers == 2:
#             previous_sum = current_sum
#         else:
#             if current_sum != previous_sum:
#                 is_all_equal = False
#         difference_between_last_two_couples = abs(current_sum - previous_sum)
#         if difference_between_last_two_couples > biggest_difference_between_two_couples:
#             biggest_difference_between_two_couples = abs(difference_between_last_two_couples)
#         previous_sum = current_sum
#         current_sum = 0
#     else:
#         current_sum += number
#
# if is_all_equal:
#     print(f"Yes, value={previous_sum}")
# else:
#     print(f"No, maxdiff={biggest_difference_between_two_couples}")