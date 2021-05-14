# 6.	Next Happy Year
# You're saying good-bye your best friend, "See you next happy year". Happy Year is the year with only distinct digits, ' \
#    '(e.g) 2018. Write a program that receives an integer number and finds the next happy year.

year = int(input())

year += 1

while True:
    year_as_string = str(year)
    if len(year_as_string) == len(set(year_as_string)):
        # See definition of set and the duplicates are not allowed part - https://www.w3schools.com/python/python_sets.asp
        # With set duplicate values are ignored
        # So if the length of len(set(year_as_string)) and len(year) are different then we have had duplicates
        print(year)
        break
    year += 1



# # # Solution without set
# year = int(input())
#
# year += 1
#
# while True:
#     is_happy = True
#     year_as_string = str(year)
#     for index_1 in range(len(year_as_string)):
#         for index_2 in range(len(year_as_string)):
#             if index_1 == index_2:
#                 continue
#             if year_as_string[index_1] == year_as_string[index_2]:
#                 is_happy = False
#                 break
#     if is_happy:
#         print(year)
#         break
#     else:
#         year += 1







