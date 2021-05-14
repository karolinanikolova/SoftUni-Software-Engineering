# 4.	Train the Trainers
# Курсът "Train the trainers" е към края си и финалното оценяване наближава.
# Вашата задача е да помогнете на журито, което ще оценява презентациите, като напишете програма,
# в която да изчислява средната оценка от представянето на всяка една презентация от даден студент,
# а накрая - средния успех от всички тях.
# От конзолата на първият ред се прочита броят на хората в журито n - цяло число.
# След това на отделен ред се прочита името на презентацията – текст.
# За всяка една презентация на нов ред се четат n - на брой оценки - реално число.
# След изчисляване на средната оценка за конкретна презентация, на конзолата се печата:
#  "{името на презентацията} - {средна оценка}."
# След получаване на команда "Finish", на конзолата се печата
# "Student's final assessment is {среден успех от всички презентации}." и програмата приключва.
# Всички оценки трябва да бъдат форматирани до втория знак след десетичната запетая.

count_assessors = int(input())
command = input()
sum_all_grades = 0
count_presentations = 0

while command != 'Finish':
    presentation_name = command
    count_grades_per_presentation = count_assessors
    sum_grades_presentation = 0
    count_presentations += 1

    for grade in range(1, count_grades_per_presentation + 1):
        grade = float(input())
        sum_grades_presentation += grade

    sum_all_grades += sum_grades_presentation

    print(f"{presentation_name} - {sum_grades_presentation / count_grades_per_presentation:.2f}.")
    command = input()

print(f"Student's final assessment is {sum_all_grades/ (count_assessors * count_presentations):.2f}.")
