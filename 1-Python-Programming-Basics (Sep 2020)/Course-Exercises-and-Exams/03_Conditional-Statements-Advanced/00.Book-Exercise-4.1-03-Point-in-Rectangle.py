# точка в правоъгълник
# Проверка дали точка {x, y} се намира вътре в правоъгълника {x1, y1} – {x2, y2}. Входните данни се четат от конзолата и се състоят от 6 реда:
# десетичните числа x1, y1, x2, y2, x и y (като се гарантира, че x1 < x2 и y1 < y2).

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x = float(input())
y = float(input())

if x1 <= x <= x2 and y1 <= y <= y2:
    print('Inside')
else:
    print('Outside')