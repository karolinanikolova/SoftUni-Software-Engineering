# 2.	Подготовка за изпит
# Напишете програма, в която Марин решава задачи от изпити, докато не получи съобщение "Enough" от лектора си.
# При всяка решена задача той получава оценка. Програмата трябва да приключи прочитането на данни при команда "Enough"
# или ако Марин получи определения брой незадоволителни оценки. Незадоволителна е всяка оценка, която е по-малка или
# равна на 4.

bad_breaks_limit = int(input())
total_score = 0
number_of_problems = 0
last_problem = ''
command = input()
number_of_bad_grades = 0
too_many_bad_grades = False

while command != 'Enough':
    last_problem = command
    current_grade = int(input())
    if current_grade <= 4:
        number_of_bad_grades += 1
        if number_of_bad_grades == bad_breaks_limit:
            too_many_bad_grades = True
            break
    number_of_problems += 1
    total_score += current_grade
    command = input()

if too_many_bad_grades:
    print(f'You need a break, {bad_breaks_limit} poor grades.')
else:
    print(f'Average score: {total_score / number_of_problems:.2f}')
    print(f'Number of problems: {number_of_problems}')
    print(f'Last problem: {last_problem}')

