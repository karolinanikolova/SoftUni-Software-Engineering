# 2.	Комбинации от букви
# Напишете програма, която да принтира на конзолата всички комбинации от 3 букви в зададен интервал,
# като се пропускат комбинациите съдържащи зададена от конзолата буква. Накрая трябва да се изпринтира броят на отпечатаните комбинации.
# Вход
# Входът се чете от конзолата и съдържа точно 3 реда:
# Ред 1.	Малка буква от английската азбука за начало на интервала – от ‘a’ до ‚z’.
# Ред 2.	Малка буква от английската азбука за край на интервала  – от първата буква до ‚z’.
# Ред 3.	Малка буква от английската азбука – от ‘a’ до ‚z’ – като комбинациите съдържащи тази буквата се пропускат.

start_letter = input()
end_letter = input()
forbidden_letter = input()
valid_combinations_counter = 0

for first_letter in range(ord(start_letter), ord(end_letter) + 1):
    for second_letter in range(ord(start_letter), ord(end_letter) + 1):
        for third_letter in range(ord(start_letter), ord(end_letter) + 1):
            if chr(first_letter) != forbidden_letter and chr(second_letter) != forbidden_letter and chr(third_letter) != forbidden_letter:
                valid_combinations_counter += 1
                print(f'{chr(first_letter)}{chr(second_letter)}{chr(third_letter)}', end = ' ')

print(valid_combinations_counter)