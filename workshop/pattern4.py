import turtle
# variable  - 변수 / multiple word - snake position? snake blabla
screen = turtle.Screen()
t = turtle.Turtle()
t.shape('turtle')
t.color('pink')

t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(200)

for i in range(3):
    t.right(120)
    t.forward(100)
    t.right(120)
    t.forward(200)


t.left(120)
t.forward(100)
t.left(120)
t.forward(200)
t.left(120)
t.forward(100)

screen.exitonclick()

