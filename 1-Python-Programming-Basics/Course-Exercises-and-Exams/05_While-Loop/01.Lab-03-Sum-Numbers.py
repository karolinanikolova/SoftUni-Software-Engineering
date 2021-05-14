# 3.	Сума от числа
# Напишете програма, която чете цяло число от конзолата и на всеки следващ ред цели числа, докато тяхната сума стане
# по-голяма или равна на първоначалното число. След приключване на четенето да се отпечата сумата на въведените числа.

number = int(input())

sum_numbers = 0

while sum_numbers < number:
    input_number = int(input())
    sum_numbers += input_number
else:
    print(sum_numbers)