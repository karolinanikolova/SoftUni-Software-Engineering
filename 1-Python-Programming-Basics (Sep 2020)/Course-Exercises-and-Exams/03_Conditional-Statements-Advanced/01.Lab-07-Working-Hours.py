# 7.	Работно време
# Да се напише програма, която чете час от денонощието(цяло число) и ден от седмицата(текст) -
# въведени от потребителя и проверява дали офисът на фирма е отворен, като работното време на офисът е от 10-18 часа, от понеделник до събота включително

time = int(input())
day = input()

if 10 <= time <= 18 and (day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday' or day == 'Saturday'):
    print('open')
else:
    print('closed')