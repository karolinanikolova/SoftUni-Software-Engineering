# 4.	Count Symbols
# Write a program that reads a text from the console and counts the occurrences of each character in it.
# Print the results in alphabetical (lexicographical) order.

# text = tuple(input())
#
# result = {}
#
# for el in text:
#     if el not in result:
#         result[el] = 1
#     else:
#         result[el] += 1

text = input()

result = {}

for char in text:
    result[char] = text.count(char)

sorted_result = sorted(result.items(), key=lambda x: x[0])

for el, value in sorted_result:
    print(f"{el}: {value} time/s")