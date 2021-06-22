# сумиране на цифрите на число
# Да се сумират цифрите на цяло положително число n. Например, ако n = 5634, то резултатът ще бъде: 5 + 6 + 3 + 4 = 18.

n = int(input())
sum_digits = 0

while True:
    last_digit = n % 10
    n = n // 10
    sum_digits += last_digit
    if n == 0:
        break

print(sum_digits)