# таблица с числа
# Да се отпечатат числата 1 … n в таблица като в примерите по-долу.

n = int(input())

for row in range(0, n):
    for col in range(0, n):
        number = row + col + 1
        if number > n:
            number = 2 * n - number
        print(number, end = ' ')
    print()

