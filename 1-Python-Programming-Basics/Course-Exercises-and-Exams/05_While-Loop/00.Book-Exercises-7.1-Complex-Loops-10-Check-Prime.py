# прости числа
# В следващата задача се изисква да направим проверка за просто число. Преди да продължим към нея,
# нека си припомним какво са простите числа.
#
# Определение: едно цяло число е просто, ако се дели без остатък единствено на себе си и на 1.
# По дефиниция простите числа са положителни и по-големи от 1. Най-малкото просто число е 2.
#
# Можем да приемем, че едно цяло число n е просто, ако n > 1 и n не се дели на число между 2 и n-1.

import math

n = int(input())
divisor = 1
prime = True

while True:
    if n % divisor == 0:
        prime = False
        break
    if divisor > math.floor(math.sqrt(n)):
        break
    divisor += 1

if prime:
    print('Prime')
else:
    print('Not prime')


# To test whether a number is prime or not, why do we have to test whether it is divisible only up to the square root of that number?
# If a number n is not a prime, it can be factored into two factors a and b:
# n = a * b
# Now a and b can't be both greater than the square root of n, since then the product a * b would be greater than ' \
# sqrt(n) * sqrt(n) = n. So in any factorization of n, at least one of the factors must be smaller than the square root
# of n, and if we can't find any factors less than or equal to the square root, n must be a prime.