# 8.	Навреме за изпит
# Студент трябва да отиде на изпит в определен час (например в 9:30 часа).
# Той идва в изпитната зала в даден час на пристигане (например 9:40).
# Счита се, че студентът е дошъл навреме, ако е пристигнал в часа на изпита или до половин час преди това.
# Ако е пристигнал по-рано повече от 30 минути, той е подранил. Ако е дошъл след часа на изпита, той е закъснял.
# Напишете програма, която прочита време на изпит и време на пристигане и отпечатва дали студентът е дошъл навреме,
# дали е подранил или е закъснял и с колко часа или минути е подранил или закъснял.

exam_hour = int(input())
exam_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())

exam_time_minutes = exam_hour * 60 + exam_minutes
arrival_time_minutes = arrival_hour * 60 + arrival_minutes
difference = exam_time_minutes - arrival_time_minutes

if 0 <= difference <= 30:
    print('On time')
elif difference > 30:
    print('Early')
elif difference < 0:
    print('Late')

if abs(difference) >= 1:
    if 0 < difference < 60:
        print(f'{abs(difference)} minutes before the start')
    elif difference >= 60:
        if abs(difference) % 60 < 10:
            print(f'{abs(difference) // 60}:0{abs(difference) % 60} hours before the start')
        else:
            print(f'{abs(difference) // 60}:{abs(difference) % 60} hours before the start')
    elif -60 < difference < 0:
        print(f'{abs(difference)} minutes after the start')
    elif difference <= -60:
        if abs(difference) % 60 < 10:
            print(f'{abs(difference) // 60}:0{abs(difference) % 60} hours after the start')
        else:
            print(f'{abs(difference) // 60}:{abs(difference) % 60} hours after the start')