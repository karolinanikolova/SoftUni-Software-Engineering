# лява и дясна сума
# Да се напише програма, която въвежда 2 * n цели числа и проверява дали сумата на първите n числа (лява сума) е
# равна на сумата на вторите n числа (дясна сума). При равенство се печата "Yes" + сумата, иначе се печата "No" + разликата.
# Разликата се изчислява като положително число (по абсолютна стойност). Форматът на изхода трябва да е като в примерите по-долу.

n = int(input())
sum_first = 0
sum_second = 0

for i in range(1, n + 1):
    current_num = float(input())
    sum_first = sum_first + current_num

for i in range(1, n + 1):
    current_num = float(input())
    sum_second = sum_second + current_num

if sum_first == sum_second:
    print('Yes, sum = %d' % sum_first)
else:
    print('No, diff = %d' % abs(sum_first - sum_second))