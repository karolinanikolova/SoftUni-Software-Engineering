# ден от седмицата
# Нека напишем програма, която принтира деня от седмицата (на английски) според въведеното число (1 … 7) или "Error",
# ако е подаден невалиден ден.

day_of_week = int(input())

if day_of_week == 1:
    print('Monday')
elif day_of_week == 2:
    print('Tuesday')
elif day_of_week == 3:
    print('Wednesday')
elif day_of_week == 4:
    print('Thursday')
elif day_of_week == 5:
    print('Friday')
elif day_of_week == 6:
    print('Saturday')
elif day_of_week == 7:
    print('Sunday')
else:
    print('Error')