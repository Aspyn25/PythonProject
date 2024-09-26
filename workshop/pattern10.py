import turtle

screen = turtle.Screen()
t = turtle.Turtle()
t.speed(0)


t.pencolor('blue')
for i in range(24):
    t.penup()
    t.forward(40)
    t.pendown()
    t.circle(25)
    t.penup()
    t.goto(0,0)
    t.left(15)


t.pencolor('red')
for i in range(24):
    t.penup()
    t.forward(50)
    t.pendown()
    t.circle(50)
    t.penup()
    t.goto(0,0)
    t.left(15)

t.hideturtle()

screen.exitonclick()