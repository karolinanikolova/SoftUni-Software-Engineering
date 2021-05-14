# 3.	Суми прости и непрости числа
# Напишете програма, която чете от конзолата цели числа, докато не се получи команда "stop".
# Да се намери сумата на всички въведени прости и сумата на всички въведени непрости числа.
# Тъй като по дефиниция от математиката отрицателните числа не могат да бъдат прости, ако на входа се подаде отрицателно
# число, да се изведе следното съобщение "Number is negative.". В този случай въведено число се игнорира и не се прибавя
# към нито една от двете суми, а програмата продължава своето изпълнение, очаквайки въвеждане на следващо число.
# На изхода да се отпечатат на два реда двете намерени суми в следния формат:
# "Sum of all prime numbers is: {prime numbers sum}"
# "Sum of all non prime numbers is: {nonprime numbers sum}"

import math
command = input()
sum_prime = 0
sum_non_prime = 0

while command != 'stop':
    number = int(command)
    is_negative = False
    is_prime = True

    if number < 0:
        is_negative = True
        print('Number is negative.')
        command = input()
        continue
        # Could also do else is_negative == False next. If we want to avoid using continue.
    if is_negative == False:
        for divisor in range(2, int(math.sqrt(number) + 1)):
            if number % divisor == 0:
                is_prime = False
                break
        if is_prime:
            sum_prime += number
        else:
            sum_non_prime += number

    command = input()

print(f'Sum of all prime numbers is: {sum_prime}')
print(f'Sum of all non prime numbers is: {sum_non_prime}')