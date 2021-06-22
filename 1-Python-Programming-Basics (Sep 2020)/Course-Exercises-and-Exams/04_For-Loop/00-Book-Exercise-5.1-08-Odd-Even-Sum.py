# четна / нечетна сума
# Да се напише програма, която въвежда n цели числа и проверява дали сумата на числата на четни позиции е равна на сумата
# на числата на нечетни позиции. При равенство печата "Yes" + сумата, иначе печата "No" + разликата.
# Разликата се изчислява по абсолютна стойност. Форматът на изхода трябва да е като в примерите по-долу.

n = int(input())
sum_even = 0
sum_odd = 0

for i in range(1, n + 1):
    current_num = int(input())
    if i % 2 == 0:
        sum_even = sum_even + current_num
    else:
        sum_odd = sum_odd + current_num

if sum_even == sum_odd:
    print('Yes')
    print(f'Sum = {sum_even}')
else:
    print('No')
    print(f'Diff = {abs(sum_even - sum_odd)}')

