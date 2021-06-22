# генератор за тъпи пароли
# Да се напише програма, която въвежда две цели числа n и l и генерира по азбучен ред всички възможни "тъпи” пароли",
# които се състоят от следните 5 символа:
#
# Символ 1: цифра от 1 до n.
# Символ 2: цифра от 1 до n.
# Символ 3: малка буква измежду първите l букви на латинската азбука.
# Символ 4: малка буква измежду първите l букви на латинската азбука.
# Символ 5: цифра от 1 до n, по-голяма от първите 2 цифри.

n = int(input())
l = int(input())
result = ''

for number1 in range(1, n):
    for number2 in range(1, n):
        for letter1 in range(ord('a'), ord('a') + l):
            for letter2 in range(ord('a'), ord('a') + l):
                for number in range(max(number1, number2) + 1, n + 1):
                    result += str(number1) + str(number2) + chr(letter1) + chr(letter2) + str(number) + ' '

print(result)

