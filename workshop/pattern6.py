import turtle

screen = turtle.Screen()
t = turtle.Turtle()
t.shape('turtle')
t.color('yellow')
for i in range(5):
    t.forward(200)
    t.right(144)

screen.exitonclick()