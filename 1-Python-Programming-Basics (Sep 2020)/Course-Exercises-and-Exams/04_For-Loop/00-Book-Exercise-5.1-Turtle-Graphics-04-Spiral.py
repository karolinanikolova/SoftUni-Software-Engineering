# чертане на спирала с костенурката
# Добавете нов Python файл spiral.py, който чертае спирала с 20 върха като на фигурата по-долу:

import turtle
my_turtle = turtle.Turtle()

my_turtle.shape('turtle')

for i in range(0, 19):
    my_turtle.right(60)
    my_turtle.forward(10 + 10 * i)

turtle.done()

