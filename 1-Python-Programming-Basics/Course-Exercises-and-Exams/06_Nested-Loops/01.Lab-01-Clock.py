# 1.	Часовник
# Напишете програма, която отпечатва часовете в денонощието от 0:0 до 23:59, всеки на отделен ред.
# Часовете трябва да се изписват във формат "{час}:{минути}".


for hour in range(0, 24):
    for minute in range(0, 60):
        print(f'{hour}:{minute}')
