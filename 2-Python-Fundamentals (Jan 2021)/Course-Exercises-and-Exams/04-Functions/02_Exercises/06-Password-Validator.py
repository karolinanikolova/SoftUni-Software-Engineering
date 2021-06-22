# 6. Password Validator
# Write a function that checks if a given password is valid. Password validations are:
# •	The length should be 6 - 10 characters (inclusive)
# •	It should consists only letters and digits
# •	It should have at least 2 digits
# If a password is valid print "Password is valid".
# If it is NOT valid, for every unfulfilled rule print a message:
# •	"Password must be between 6 and 10 characters"
# •	"Password must consist only of letters and digits"
# •	"Password must have at least 2 digits"

# def check_if_password_valid(input_pass):
#     count_digits = 0
#     is_valid = True
#
#     if len(input_pass) < 6 or len(input_pass) > 10:
#         print('Password must be between 6 and 10 characters')
#         is_valid = False
#
#     for char in input_pass:
#         if ord(char) < 48 or 57 < ord(char) < 65 or 90 < ord(char) < 97 or ord(char) > 122:
#             print('Password must consist only of letters and digits')
#             is_valid = False
#             if not is_valid:
#                 break
#
#     for char in input_pass:
#         if 48 <= ord(char) <= 57:
#             count_digits += 1
#
#     if count_digits < 2:
#         print('Password must have at least 2 digits')
#         is_valid = False
#
#     if is_valid:
#         print('Password is valid')
#
#
# password = input()
#
# result = check_if_password_valid(password)

def check_if_password_valid(input_pass):
    count_digits = 0
    is_valid = True

    if len(input_pass) < 6 or len(input_pass) > 10:
        print('Password must be between 6 and 10 characters')
        is_valid = False

    # for char in input_pass:
    #     if not char.isdigit() and not char.isalpha():
    #         is_valid = False
    #         print('Password must consist only of letters and digits')
    #
    #     if not is_valid:
    #         break

    if not input_pass.isalnum():
        is_valid = False
        print('Password must consist only of letters and digits')

    for char in input_pass:
        if char.isdigit():
            count_digits += 1

    if count_digits < 2:
        print('Password must have at least 2 digits')
        is_valid = False

    return is_valid


password = input()

result = check_if_password_valid(password)

if result:
    print('Password is valid')

