# 3.	Щастливи числа
# Да се напише програма, която прочита едно цяло число N и генерира всички възможни "щастливи" и
# различни 4-цифрени числа(всяка цифра от числото е в интервала [1...9]).
# Числото трябва да отговаря на следните условия:
# Щастливо число е 4-цифрено число, на което сбора от първите две цифри е равен на сбора от последните две.
# Числото N трябва да се дели без остатък от сбора на първите две цифри на "щастливото" число.

N = int(input())

for first_number in range(1, 10):
    for second_number in range(1, 10):
        if N % (first_number + second_number) != 0:
            continue
        else:
            for third_number in range(1, 10):
                for fourth_number in range(1, 10):
                    if first_number + second_number == third_number + fourth_number:
                        print(f'{first_number}{second_number}{third_number}{fourth_number}', end= ' ')


