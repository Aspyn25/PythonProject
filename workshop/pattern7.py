import turtle

screen = turtle.Screen()
t = turtle.Turtle()
t.shape('turtle')
t.color('blue')
screen.bgcolor('green')
turtle.color("blue")



t.goto(0,0)
t.penup()
t.forward(100)
t.pendown()
t.pensize(3)
t.forward(20)
t.penup()
t.forward(20)
t.stamp()
t.home()

for i in range(11):
    t.left(30)
    t.penup()
    t.forward(100)
    t.pendown()
    t.pensize(3)
    t.forward(20)
    t.penup()
    t.forward(20)
    t.stamp()
    t.goto(0,0)

t.left(30)

screen.exitonclick()