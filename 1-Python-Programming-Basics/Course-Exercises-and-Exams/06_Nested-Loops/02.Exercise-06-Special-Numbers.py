# 6.	Специални числа
# Да се напише програма, която чете едно цяло число N, въведено от потребителя, и генерира всички възможни "специални"
# числа от 1111 до 9999. За да бъде “специално” едно число, то трябва да отговаря на следното условие:
# •	N да се дели на всяка една от неговите цифри без остатък.
# Пример: при N = 16, 2418 е специално число:
# •	16 / 2 = 8 без остатък
# •	16 / 4 = 4 без остатък
# •	16 / 1 = 16 без остатък
# •	16 / 8 = 2 без остатък

N = int(input())

for number in range(1111, 9999 + 1):
    is_number_special = True
    number_as_string = str(number)
    # Could also write for index, digit in enumerate(number_as_string): but since we don't need the index we don't need enumerate.
    for digit in number_as_string:
        if int(digit) == 0 or N % int(digit) != 0:
            is_number_special = False
            break
    if is_number_special:
        print(f'{number_as_string}', end = ' ')



