# 10.	Прогноза за времето – част 2
# Напишете програма, която при въведени градуси (реално число) принтира какво е времето, като имате предвид следната таблица:
# Градуси	Време
# 26.00 - 35.00	Hot
# 20.1 - 25.9	Warm
# 15.00 - 20.00	Mild
# 12.00 - 14.9	Cool
# 5.00 - 11.9	Cold
# Ако се въведат градуси, различни от посочените в таблицата, да се отпечата "unknown".

weather = float(input())

if 26.00 <= weather <= 35.00:
    print(f"Hot")
elif 20.1 <= weather <= 25.9:
    print(f"Warm")
elif 15.00 <= weather <= 20.00:
    print(f"Mild")
elif 12.00 <= weather <= 14.9:
    print(f"Cool")
elif 5.00 <= weather <= 11.9:
    print(f"Cold")
else:
    print("unknown")