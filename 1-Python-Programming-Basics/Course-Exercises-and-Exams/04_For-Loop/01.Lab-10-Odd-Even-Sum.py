# 10.	Четна / нечетна сума
# Да се напише програма, която чете n-на брой цели числа, подадени от потребителя, и проверява дали сумата от числата
# на четни позиции е равна на сумата на числата на нечетни позиции. При равенство да се отпечатат два реда: "Yes" и на
# нов ред "Sum = " + сумата; иначе да се отпечата "No" и на нов ред "Diff = " + разликата. Разликата се изчислява по
# абсолютна стойност.

n = int(input())
sum_even = 0
sum_odd = 0

for number_index in range(1, n + 1):
    number_value = int(input())
    if number_index % 2 == 0:
        sum_even += number_value
    else:
        sum_odd += number_value

if sum_even == sum_odd:
    print('Yes')
    print(f'Sum = {sum_even}')
else:
    print('No')
    print(f'Diff = {abs(sum_even - sum_odd)}')

