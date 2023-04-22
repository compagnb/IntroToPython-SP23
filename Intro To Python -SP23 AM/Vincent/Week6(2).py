import turtle
bob=turtle.Turtle()
bob.color("red")
bob.shape("square")
bob.left(72)
for i in range(0,6):
    bob.forward(100)
    bob.right(144)
    bob.forward(200)
    bob.right(72)
    bob.forward(100)


def pentagram(a,b,c):
    bob.penup()
    bob.goto(b,c)
    bob.pendown()
    for i in range(0,6):
        bob.forward(a)
        bob.right(144)
        bob.forward(2*a)
        bob.right(72)
        bob.forward(a)
pentagram(300,-50,-200)

