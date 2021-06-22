# 5. Palindrome Integers
# A palindrome is a number which reads the same backward as forward, such as 323 or 1001.
# Write a function which receives a list of positive integers and checks if each integer is a palindrome or not.
# Print the results on the console
# The input will be a single string containing the numbers separated by comma and space ", "

def check_and_print_if_palindrome(el):
    if el == el[::-1]:
        return True
    return False


nums_as_string_in_list = input().split(', ')

for num_as_string in nums_as_string_in_list:
    print(check_and_print_if_palindrome(num_as_string))

