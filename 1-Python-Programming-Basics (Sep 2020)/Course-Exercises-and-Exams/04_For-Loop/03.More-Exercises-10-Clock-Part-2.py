# 10.	Часовник – част 2
# Напишете програма, която да отпечатва часовете в денонощието от 0:0:0 до 23:59:59, всеки на отделен ред.
# Часовете да се изписват във формат "{час} : {минути} : {секунди} ".

hours = 23
minutes = 59
seconds = 59

for hour in range(0, hours + 1):
    for minute in range(0, minutes + 1):
        for second in range(0, seconds + 1):
            print(f'{hour} : {minute} : {second}')
