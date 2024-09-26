import turtle

screen = turtle.Screen()
t = turtle.Turtle()

for a in range(10):
    for b in range(10):
        t.pencolor('blue')
        t.forward(25)
        t.left(36)
    t.left(36)

for j in range(10):
    for i in range(5):
        t.pencolor('red')
        t.forward(50)
        t.left(72)
    t.left(36)



screen.exitonclick()