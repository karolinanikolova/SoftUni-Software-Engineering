# 8.	* Mutate Strings
# You will be given two strings. Transform the first string into the second one, one letter at a time and print it.
# Print only the unique strings
# Note: the strings will have the same lengths

str_1 = input()
str_2 = input()

n = len(str_1)
previous_str = str_1
str_output = ''

for index in range(n + 1):
    str_output = str_2[0:index] + str_1[index:n]
    if not str_output == previous_str:
        print(str_output)
    previous_str = str_output



# # Longer solution which lecturer showed
# starting_word = input()
# aim_mutated_word = input()
#
# result = ""
# previous_str = starting_word
#
# for index in range(len(starting_word)):
#     for i in range(index + 1):
#         result += aim_mutated_word[i]
#     for i in range(index + 1, len(aim_mutated_word)):
#         result += starting_word[i]
#     if not result == previous_str:
#         print(result)
#     previous_str = result
#     result = ""