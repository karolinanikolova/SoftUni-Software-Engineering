# 1.	Числа до 1000, завършващи на 7
# Напишете програма, която отпечатва числата в диапазона [1…1000], които завършват на 7.

for number in range(1, 1001):
    if number % 10 == 7:
        print(number)