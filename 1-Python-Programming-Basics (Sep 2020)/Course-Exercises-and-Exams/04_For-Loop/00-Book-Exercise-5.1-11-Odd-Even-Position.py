# четни / нечетни позиции
# Напишете програма, която чете n числа и пресмята сумата, минимума и максимума на числата на четни и нечетни позиции
# (броим от 1). Когато няма минимален / максимален елемент, отпечатайте "No".

import sys

n = int(input())
sum_even = 0
sum_odd = 0
max_even = - sys.maxsize
min_even = sys.maxsize
max_odd = - sys.maxsize
min_odd = sys.maxsize
is_valid = True

for i in range(1, n + 1):
    current_number = float(input())
    if i % 2 == 0:
        sum_even += current_number
        if current_number > max_even:
            max_even = current_number
        if current_number < min_even:
            min_even = current_number
    else:
        sum_odd += current_number
        if current_number > max_odd:
            max_odd = current_number
        if current_number < min_odd:
            min_odd = current_number


print(f'OddSum=%g,' % sum_odd)

if min_odd == sys.maxsize:
    print('OddMin=No,')
else:
    print('OddMin=%g,' % min_odd)

if max_odd == - sys.maxsize:
    print('OddMax=No,')
else:
    print('OddMax=%g,' % max_odd)

print(f'EvenSum=%g,' % sum_even)

if min_even == sys.maxsize:
    print('EvenMin=No,')
else:
    print('EvenMin=%g,' % min_even)

if max_even == - sys.maxsize:
    print('EvenMax=No')
else:
    print('EvenMax=%g' % max_even)
