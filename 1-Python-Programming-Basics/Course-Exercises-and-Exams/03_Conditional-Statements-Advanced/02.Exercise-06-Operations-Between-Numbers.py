# 6.	Операции между числа
# Напишете програма, която чете две цели числа (N1 и N2) и оператор, с който да се извърши дадена математическа операция. Възможните операции са:
# Събиране(+), Изваждане(-), Умножение(*),  Деление(/) и Модулно деление(%).
# При събиране, изваждане и умножение на конзолата трябва да се отпечатат резултата и дали той е четен или нечетен.
# При обикновеното деление – резултата. При модулното деление – остатъка. Трябва да се има предвид, че делителят може да е равен на 0 (нула),
# а на нула не се дели. В този случай трябва да се отпечата специално съобщениe.

first_number = int(input())
second_number = int(input())
operator = input()
result = 0

if operator == '+':
    result = first_number + second_number
    if result % 2 == 0:
        print(f'{first_number} {operator} {second_number} = {result} - even')
    else:
        print(f'{first_number} {operator} {second_number} = {result} - odd')
elif operator == '-':
    result = first_number - second_number
    if result % 2 == 0:
        print(f'{first_number} {operator} {second_number} = {result} - even')
    else:
        print(f'{first_number} {operator} {second_number} = {result} - odd')
elif operator == '*':
    result = first_number * second_number
    if result % 2 == 0:
        print(f'{first_number} {operator} {second_number} = {result} - even')
    else:
        print(f'{first_number} {operator} {second_number} = {result} - odd')
elif operator == '/':
    if second_number != 0:
        result = first_number / second_number
        print(f'{first_number} {operator} {second_number} = {result:.2f}')
    else:
        print(f'Cannot divide {first_number} by zero')
elif operator == '%':
    if second_number != 0:
        result = first_number % second_number
        print(f'{first_number} {operator} {second_number} = {result}')
    else:
        print(f'Cannot divide {first_number} by zero')