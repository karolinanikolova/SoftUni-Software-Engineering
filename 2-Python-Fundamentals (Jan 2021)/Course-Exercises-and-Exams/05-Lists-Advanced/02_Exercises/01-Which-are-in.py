# 1.	Which Are In?
# Given two lists of strings print a new list of the strings that contains words from the first list which are substrings
# of any of the strings in the second list (only unique values)

first_string = input().split(", ")
second_string = input().split(", ")

result = []

result = [el_1 for el_1 in first_string for el_2 in second_string if el_1 in el_2]

# for el_1 in first_string:
#     for el_2 in second_string:
#         if el_1 in el_2:
#             result.append(el_1)

print(sorted(set(result), key = result.index))