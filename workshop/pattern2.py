import turtle
# variable  - 변수 / multiple word - snake position? snake blabla
screen = turtle.Screen()
t = turtle.Turtle()
t.shape('turtle')
t.color('blue')

t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)

t.penup()
t.goto(50,-25)
t.pendown()
t.left(45)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)

screen.exitonclick()

