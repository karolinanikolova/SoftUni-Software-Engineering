# 8.	Завършване – част 2
# Напишете програма, която изчислява средната оценка на ученик от цялото му обучение.
# На първия ред ще получите името на ученика, а на всеки следващ ред - неговите годишни оценки.
# Ученикът преминава в следващия клас, ако годишната му оценка е по-голяма или равна на 4.00.
# Ако ученикът бъде скъсан повече от един път, то той бива изключен и програмата приключва,
# като се отпечатва името на ученика и в кой клас е изключен.
#  При успешно завършване на 12-ти клас да се отпечата :
# "{име на ученика} graduated. Average grade: {средната оценка от цялото обучение}"
# В случай, че ученикът е изключен от училище, да се отпечата:
# "{име на ученика} has been excluded at {класа, в който е бил изключен} grade"
# Стойността трябва да бъде форматирана до втория знак след десетичната запетая.

name = input()
count_fail = 0
grade_count = 0
grade_total = 0
average_grade = 0
isFail = False

while grade_count < 12:
    grade = float(input())
    grade_total += grade
    grade_count += 1
    if grade < 4.00:
        count_fail += 1
    if count_fail > 1:
        isFail = True
        break

if isFail:
    print(f'{name} has been excluded at {grade_count - 1} grade')
else:
    average_grade = grade_total / grade_count
    print(f'{name} graduated. Average grade: {average_grade:.2f}')


