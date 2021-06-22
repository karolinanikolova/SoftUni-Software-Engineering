# 1.	Уникални PIN кодове
# Да се напише програма, която генерира трицифрени PIN кодове, като цифрите на всеки PIN код са в определен интервал.
# За да бъде валиден един PIN код той трябва да отговаря на следните условия:
# •	Първата и третата цифра трябва да бъдат четни.
# •	Втората цифра трябва да бъде просто число в диапазона [2...7].
# Вход
# От конзолата се четат 3 реда:
# •	Горната граница на първото число - цяло число в диапазона [1...9]
# •	Горната граница на второто число - цяло число в диапазона [1...9]
# •	Горната граница на третото число - цяло число в диапазона [1...9]

top_boundary_first_digit = int(input())
top_boundary_second_digit = int(input())
top_boundary_third_digit = int(input())

for first_digit in range(1, top_boundary_first_digit + 1):
    if first_digit % 2 != 0:
        continue
    for second_digit in range(1, top_boundary_second_digit + 1):
        is_second_digit_prime = True
        if second_digit < 2 or second_digit > 7:
            continue
        else:
            for divisor in range(2, second_digit):
                if second_digit % divisor == 0:
                    is_second_digit_prime = False
        for third_digit in range(1, top_boundary_third_digit + 1):
            if third_digit % 2 != 0:
                continue
            if is_second_digit_prime:
                print(f'{first_digit} {second_digit} {third_digit}')

