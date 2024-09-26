import turtle
# variable  - 변수 / multiple word - snake position? snake blabla

degree = 360/5
screen = turtle.Screen()
t = turtle.Turtle()
t.shape('turtle')
t.color('pink')

for i in range(5):

    t.left(degree)
    t.forward(50)
    t.right(90)

    t.forward(100)
    t.right(90)

    t.forward(100)
    t.right(90)

    t.forward(100)
    t.right(90)

    t.forward(50)



screen.exitonclick()

