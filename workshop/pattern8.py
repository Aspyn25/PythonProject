import turtle

screen = turtle.Screen()
t = turtle.Turtle()
num = 0
for i in range(19):
    num = num + 10
    t.right(144)
    t.forward(num)

t.right(144)



screen.exitonclick()