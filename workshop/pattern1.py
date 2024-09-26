import turtle
# variable  - 변수 / multiple word - snake position? snake blabla
screen = turtle.Screen()
t = turtle.Turtle()
t.shape('turtle')
t.color('red')

t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)

t.penup()
t.goto(-10,-10)
t.pendown()
t.pensize(10)
t.forward(120)
t.left(90)
t.forward(120)
t.left(90)
t.forward(120)
t.left(90)
t.forward(120)

screen.exitonclick()

