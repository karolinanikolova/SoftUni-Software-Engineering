# 3.	Next Version
# You're fed up about changing the version of your software manually. ' \
#    'Instead, you will create a little script that will make it for you.
# You will be given a version as in this example: "1.3.4".
# You have to find the next version and print it ("1.3.5" from the example).
# The only rule is that the numbers cannot be greater than 9.
# If that happens, set the current number to 0 and increase the number before it. For more clarification, see the examples.
# ote: there will be no case where the first number will get greater than 9

input_version_as_list = input().split(".")

input_version_as_int = int("".join(input_version_as_list))
output_version_as_int = input_version_as_int + 1

output_version_as_string = ".".join(str(output_version_as_int))

print(output_version_as_string)

# input_version = list(map(int, input().split(".")))
#
# output_version = input_version
#
# if input_version[2] < 9:
#     output_version[2] += 1
# else:
#     if input_version[1] < 9:
#         output_version[2] = 0
#         output_version[1] += 1
#     else:
#         output_version[2] = 0
#         output_version[1] = 0
#         output_version[0] += 1
#
# output_version = list(map(str, output_version))
#
# print(".".join(output_version))

