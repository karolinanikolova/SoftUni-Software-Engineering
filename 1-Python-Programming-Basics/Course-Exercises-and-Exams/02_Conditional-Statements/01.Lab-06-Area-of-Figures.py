# 6.	Лица на фигури
# Да се напише програма, в която потребителят въвежда вида и размерите на геометрична фигура и пресмята лицето й.
# Фигурите са четири вида: квадрат (square), правоъгълник (rectangle), кръг (circle) и триъгълник (triangle).
# На първия ред на входа се чете вида на фигурата (square, rectangle, circle или triangle):
# •	Ако фигурата е квадрат, на следващия ред се чете едно число - дължина на страната му;
# •	Ако фигурата е правоъгълник, на следващите два реда четат две числа - дължините на страните му;
# •	Ако фигурата е кръг, на следващия ред чете едно число - радиусът на кръга;
# •	Ако фигурата е триъгълник, на следващите два реда четат две числа - дължината на страната му и дължината на височината към нея.
# Резултатът да се закръгли до 3 цифри след десетичната точка.

import math

type = input()

if type == "square":
    a = float(input())
    area_square = math.pow(a, 2) # a * a
    print(f"{area_square:.3f}")
elif type == "rectangle":
    a = float(input())
    b = float(input())
    area_rectangle = a * b
    print(f"{area_rectangle:.3f}")
elif type == "circle":
    r = float(input())
    area_circle = math.pi * r * r
    print(f"{area_circle:.3f}")
elif type == "triangle":
    a = float(input())
    h = float(input())
    area_triangle = a * h / 2
    print(f"{area_triangle:.3f}")