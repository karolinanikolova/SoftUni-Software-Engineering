# чертане на звезда с костенурката
# Добавете нов Python файл star.py, който чертае звезда с 5 върха (петолъчка), като на фигурата по-долу:

import turtle
my_turtle = turtle.Turtle()

#  Change the shape of the turtle
my_turtle.shape("turtle")

#  Change color of pen and turtle
my_turtle.color("green")

for i in range(1, 6):
        my_turtle.forward(200)
        my_turtle.left(144)

turtle.done()