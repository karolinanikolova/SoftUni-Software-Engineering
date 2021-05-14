# по-голямото число
# Да се напише програма, която чете две цели числа и извежда по-голямото от тях.
#
# Първата ни подзадача е да прочетем двете числа. След което, чрез проста if-else конструкция, в съчетание с оператора за по-голямо (>), да направим проверка.

print("Enter two integers:")
firstNumber = int(input())
secondNumber = int(input())

if firstNumber >= secondNumber:
    print(firstNumber)
else:
    print(secondNumber)