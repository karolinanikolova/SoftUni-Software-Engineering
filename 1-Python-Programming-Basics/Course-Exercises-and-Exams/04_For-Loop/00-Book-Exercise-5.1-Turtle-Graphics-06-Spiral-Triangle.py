import turtle
my_turtle = turtle.Turtle()

my_turtle.shape('turtle')

for i in range(0, 21):
    my_turtle.left(120)
    my_turtle.forward(10 + 10 * i)

my_turtle.right(120)

for i in range(0, 21):
    my_turtle.forward(10 + 10 * i)
    my_turtle.left(120)

my_turtle.left(120)

for i in range(0, 21):
    my_turtle.forward(10 + 10 * i)
    my_turtle.left(120)

turtle.done()