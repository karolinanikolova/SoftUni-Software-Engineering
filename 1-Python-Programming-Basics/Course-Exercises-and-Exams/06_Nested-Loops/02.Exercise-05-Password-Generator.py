# 5.	Генератор за пароли
# Да се напише програма, която чете две цели числа n и l, въведени от потребителя, и генерира по азбучен ред всички
# възможни  пароли, които се състоят от следните 5 символа:
# •	Символ 1: цифра от 1 до n;
# •	Символ 2: цифра от 1 до n;
# •	Символ 3: малка буква измежду първите l букви на латинската азбука;
# •	Символ 4: малка буква измежду първите l букви на латинската азбука;
# •	Символ 5: цифра от 1 до n, по-голяма от първите 2 цифри.

n = int(input())
l = int(input())

for symbol_one in range(1, n + 1):
    for symbol_two in range(1, n + 1):
        for symbol_three in range(ord('a'), ord('a') + l):
            for symbol_four in range(ord('a'), ord('a') + l):
                for symbol_five in range(1, n + 1):
                    if symbol_five <= symbol_one or symbol_five <= symbol_two:
                        continue
                    print(f'{symbol_one}{symbol_two}{chr(symbol_three)}{chr(symbol_four)}{symbol_five }', end = ' ')

