# 5.	Баланс по сметка
# Напишете програма, която пресмята колко общо пари има в сметката, след като направите определен брой вноски.
# На всеки ред ще получавате сумата, която трябва да внесете в сметката до получаване на команда “NoMoreMoney”.
# При всяка получена сума на конзолата трябва да се извежда "Increase: " + сумата и тя да се прибавя в сметката.
# Ако получите число по-малко от 0 на конзолата трябва да се изведе "Invalid operation!" и програмата да приключи.
# Когато програмата приключи трябва да се принтира "Total: " + общата сума в сметката закръглена до втория знак след
# десетичната запетая.

account_input = input()
sum = 0

while account_input != 'NoMoreMoney':
    account_input = float(account_input)
    if account_input < 0:
        print(f'Invalid operation!')
        print(f'Total: {sum:.2f}')
        break
    increase = account_input
    sum += account_input
    print(f'Increase: {increase:.2f}')
    account_input = input()
else:
    print(f'Total: {sum:.2f}')