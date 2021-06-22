# 1.	Пирамида от числа
# Напишете програма, която чете цяло число n, въведено от потребителя, и отпечатва пирамида от числа като в примерите:
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15


# With boolean
n = int(input())
number_for_printing = 1
all_is_printed = False

for row in range (1, n + 1):
    # number of columns = number of rows
    for col in range (1, row + 1):
        print(f'{number_for_printing}', end = ' ')
        number_for_printing += 1
        if number_for_printing > n:
            all_is_printed = True
            break
    if all_is_printed:
        break
    print()

# # Without boolean
# n = int(input())
# number_for_printing = 1
#
# for row in range (1, n + 1):
#     # number of columns = number of rows
#     for col in range (1, row + 1):
#         print(f'{number_for_printing}', end = ' ')
#         number_for_printing += 1
#         if number_for_printing > n:
#             break
#     if number_for_printing > n:
#         break
#     print()



