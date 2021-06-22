# 7.	*Билети за кино
# Вашата задача е да напишете програма, която да изчислява процента на билетите за всеки тип от продадените билети:
# студентски(student), стандартен(standard) и детски(kid), за всички прожекции. Трябва да изчислите и колко процента
# от залата е запълнена за всяка една прожекция.

command = input()
tickets_sold_total = 0
tickets_sold_total_student = 0
tickets_sold_total_standard = 0
tickets_sold_total_kid = 0
ticket_type = ''

while command != 'Finish':
    initial_free_spaces = int(input())
    free_spaces = initial_free_spaces
    tickets_sold_this_projection = 0
    while free_spaces > 0:
        ticket_type = input()
        if ticket_type == 'End':
            break
        elif ticket_type == 'student':
            tickets_sold_total_student += 1
        elif ticket_type == 'standard':
            tickets_sold_total_standard += 1
        elif ticket_type == 'kid':
            tickets_sold_total_kid += 1
        free_spaces -= 1
        tickets_sold_total += 1
        tickets_sold_this_projection += 1
    print(f"{command} - {tickets_sold_this_projection / initial_free_spaces * 100:.2f}% full.")

    command = input()

print(f'Total tickets: {tickets_sold_total}')
print(f"{tickets_sold_total_student / tickets_sold_total * 100:.2f}% student tickets.")
print(f"{tickets_sold_total_standard / tickets_sold_total * 100:.2f}% standard tickets.")
print(f"{tickets_sold_total_kid / tickets_sold_total * 100:.2f}% kids tickets.")

