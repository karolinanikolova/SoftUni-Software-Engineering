# 9.	Часовник
# Напишете програма, която отпечатва часовете в денонощието от 0:0 до 23:59, всеки на отделен ред.
# Часовете трябва да се изписват във формат "{час} : {минути}".

hours = 23
minutes = 59

for hour in range(0, hours + 1):
    for minute in range(0, minutes + 1):
        print(f'{hour} : {minute}')