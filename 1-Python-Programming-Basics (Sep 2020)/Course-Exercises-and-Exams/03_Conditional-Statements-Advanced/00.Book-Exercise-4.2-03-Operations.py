# операции между числа
# Напишете програма, която чете две цели числа (n1 и n2) и оператор, с който да се извърши дадена математическа операция
# с тях. Възможните операции са: събиране (+), изваждане (-), умножение (*), деление (/) и модулно деление (%).
# При събиране, изваждане и умножение на конзолата трябва да се отпечата резултата и дали той е четен или нечетен.
# При обикновено деление – единствено резултата, а при модулно деление – остатъка. Трябва да се има предвид, че
# делителят може да е равен на нула (= 0), а на нула не се дели. В този случай трябва да се отпечата специално съобщение.
#
# Входни данни
# От конзолата се прочитат 3 реда:
#
# N1 – цяло число в интервала [0 … 40 000].
# N2 – цяло число в интервала [0 … 40 000].
# Оператор – един символ измежду: "+", "-", "*", "/", "%".

first_number = int(input())
second_number = int(input())
operator = input()
result = 0

if operator == '+':
    result = first_number + second_number
    if result % 2 == 0:
        output = f'{first_number} {operator} {second_number} = {result} - even'
    else:
        output = f'{first_number} {operator} {second_number} = {result} - odd'
elif operator == '-':
    result = first_number - second_number
    if result % 2 == 0:
        output = f'{first_number} {operator} {second_number} = {result} - even'
    else:
        output = f'{first_number} {operator} {second_number} = {result} - odd'
elif operator == '*':
    result = first_number * second_number
    if result % 2 == 0:
        output = f'{first_number} {operator} {second_number} = {result} - even'
    else:
        output = f'{first_number} {operator} {second_number} = {result} - odd'
elif operator == '/':
    if second_number != 0:
        result = first_number / second_number
        output = f'{first_number} {operator} {second_number} = {result:.2f}'
    else:
        output = f'Cannot divide {first_number} by zero'
elif operator == '%':
    if second_number != 0:
        result = first_number % second_number
        output = f'{first_number} {operator} {second_number} = {result}'
    else:
        output = f'Cannot divide {first_number} by zero'

print(output)