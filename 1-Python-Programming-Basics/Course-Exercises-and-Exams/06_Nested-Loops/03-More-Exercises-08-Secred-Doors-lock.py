# 8.	Отключване на тайната врата
# В града има тайна врата, за която всички знаят, но никой не е успявал да я отключи и да види какво има зад нея.
# За да бъде отключена трябва да се въведе трицифрен код.
# Напишете програма, която генерира комбинации спрямо въведени числа – предположения от потребителя.
# От конзолата се въвеждат три цифри. Тези цифри ще бъдат горната граница, до която ние искаме да получим всички
# трицифрени числа, на които всяка една цифра отговаря на следните условия:
# •	Цифрата на единиците и цифрата на стотиците трябва да бъде четна
# •	Цифрата на десетиците да бъде просто число в диапазона (2...7).
# Това ще са възможните комбинации според въведените предположения от потребителя, с които ще може евентуално
# да се отключи вратата.

first_digit_top_boundary = int(input())
second_digit_top_boundary = int(input())
third_digit_top_boundary = int(input())

for first_digit in range(1, first_digit_top_boundary + 1):
    for second_digit in range(2, second_digit_top_boundary + 1):
        is_second_digit_prime = True
        for divisor in range(2, second_digit):
            if second_digit % divisor == 0:
                is_second_digit_prime = False
        for third_digit in range(1, third_digit_top_boundary + 1):
            if first_digit % 2 == 0 and third_digit % 2 == 0 and is_second_digit_prime:
                print(f'{first_digit} {second_digit} {third_digit}')
