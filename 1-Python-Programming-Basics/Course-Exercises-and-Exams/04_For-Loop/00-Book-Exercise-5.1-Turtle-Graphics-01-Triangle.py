# чертане с костенурка – графично GUI приложение
# Целта на следващото упражнение е да си поиграем с една библиотека за рисуване, известна като "графика с костенурка"
# (turtle graphics). Ще изградим графично приложение, в което ще рисуваме различни фигури, придвижвайки нашата
# "костенурка" по екрана чрез операции от типа "отиди напред 100 позиции", "завърти се надясно на 30 градуса",
# "отиди напред още 50 позиции".

# За чертането ще използваме външната библиотека turtle. Тя дефинира клас Turtle, който представлява костенурка за
# рисуване. За да я използваме, добавяме следния код, най-отгоре в началото на Python файла:

import turtle
my_turtle = turtle.Turtle()

#  Change the shape of the turtle
my_turtle.shape("turtle")

for i in range(0, 3):
    # Draw a equilateral triangle
    my_turtle.left(30)
    my_turtle.forward(200)
    my_turtle.left(120)
    my_turtle.forward(200)
    my_turtle.left(120)
    my_turtle.forward(200)

    # Draw a line in the rectangle
    my_turtle.left(-30)
    my_turtle.penup()
    my_turtle.backward(50)
    my_turtle.pendown()
    my_turtle.backward(100)
    my_turtle.penup()
    my_turtle.forward(150)
    my_turtle.pendown()
    my_turtle.left(30)

turtle.done()