# чертане на слънце с костенурката
# Добавете нов Python файл sun.py, който чертае слънце с 36 върха като на фигурата по-долу:

import turtle

my_turtle = turtle.Turtle()

my_turtle.shape('turtle')

for i in range(0, 37):
    my_turtle.left(1)
    my_turtle.forward(100)
    my_turtle.left(160)
    my_turtle.forward(100)

turtle.done()