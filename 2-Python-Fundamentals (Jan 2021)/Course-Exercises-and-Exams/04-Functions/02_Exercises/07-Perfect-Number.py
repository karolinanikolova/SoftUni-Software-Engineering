# 7. Perfect Number
# Write a function that receives an integer number and returns if this number is perfect or NOT.
# A perfect number is a positive integer that is equal to the sum of its proper positive divisors.
# That is the sum of its positive divisors excluding the number itself (also known as its aliquot sum).

# def check_if_number_perfect(num):
#     aliquot_sum = 0
#
#     for digit in range(1, num):
#         if num % digit == 0:
#             aliquot_sum += digit
#
#     if aliquot_sum == num:
#         return True
#     return False
#
#
# number = int(input())
#
# result = check_if_number_perfect(number)
#
# if result:
#     print('We have a perfect number!')
# else:
#     print('It\'s not so perfect.')

def check_if_number_perfect(num):
    proper_divisors = []

    for digit in range(1, num):
        if num % digit == 0:
            proper_divisors.append(digit)

    if sum(proper_divisors) == num:
        return True
    return False


number = int(input())

result = check_if_number_perfect(number)

if result:
    print('We have a perfect number!')
else:
    print('It\'s not so perfect.')
