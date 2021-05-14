# пирамида от числа
# Да се отпечатат числата 1 … n в пирамида като в примерите по долу.
# На първия ред печатаме едно число, на втория ред печатаме две числа, на третия ред печатаме три числа и т.н.
# докато числата свършат. На последния ред печатаме толкова числа, колкото останат докато стигнем до n.

n = int(input())

number = 1

for row in range(1, n + 1):
    for col in range(1, row + 1):
        print(number, end = ' ')
        number += 1
        if col >= row:
            print()
        if number > n:
            break
    if number > n:
        break