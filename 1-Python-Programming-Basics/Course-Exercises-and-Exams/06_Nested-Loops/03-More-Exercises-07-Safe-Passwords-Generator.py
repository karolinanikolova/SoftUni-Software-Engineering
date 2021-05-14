# 7.	Генератор за сигурни пароли
# Ани се страхува от това, да не й бъде хакнат някой от профилите в социалните мрежи, затова решава да направи генератор
# за пароли, които да бъдат достатъчно сигурни. Вашата задача е да й помогнете да напише програма, която ще генерира тези
# пароли, разделени една от друга от знака "|".
# Да се напише програма, която генерира серия от символи като в шаблона:
# ABxyBA
# като при всяко генериране на нов код, стойностите на символите се увеличават с 1. Ако A надхвърли 55, се връща на 35.
# Ако B надхвърли 96, се връща на 64.

a = int(input())
b = int(input())
max_number_generated_passwords = int(input())
first_symbol = 35
second_symbol = 64
counter_generated_passwords = 0

while first_symbol <= 55 and second_symbol <= 96:
    for third_symbol in range(1, a + 1):
        for fourth_symbol in range(1, b + 1):
            fifth_symbol = second_symbol
            sixth_symbol = first_symbol
            counter_generated_passwords += 1
            if counter_generated_passwords <= max_number_generated_passwords:
                print(f'{chr(first_symbol)}{chr(second_symbol)}{third_symbol}{fourth_symbol}{chr(fifth_symbol)}{chr(sixth_symbol)}|', end='')
            if counter_generated_passwords == max_number_generated_passwords:
                break
            first_symbol += 1
            second_symbol += 1
            if first_symbol == 56:
                first_symbol = 35
            if second_symbol == 97:
                second_symbol = 64

    if third_symbol == a or fourth_symbol == b:
        break


# while True:
#     for first_symbol in range(35, 56):
#         for second_symbol in range(64, 97):
#             for third_symbol in range(1, a + 1):
#                 for fourth_symbol in range(1, b + 1):
#                     fifth_symbol = second_symbol
#                     sixth_symbol = first_symbol
#                     if counter_generated_passwords <= max_number_generated_passwords and third_symbol <= a and fourth_symbol <= b:
#                         counter_generated_passwords += 1
#                         print(f'{chr(first_symbol)}{chr(second_symbol)}{third_symbol}{fourth_symbol}{chr(fifth_symbol)}{chr(sixth_symbol)}|', end='')
#                     else:
#                         break