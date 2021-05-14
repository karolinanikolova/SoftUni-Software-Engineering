# чертане на шестоъгълник с костенурката
# Добавeте нов Python файл, с примерно име hexagon, който ще чертае правилен шестоъгълник:


import turtle
my_turtle = turtle.Turtle()

#  Change the shape of the turtle
my_turtle.shape("turtle")

for i in range(1, 7):
        my_turtle.forward(100)
        my_turtle.left(60)

turtle.done()