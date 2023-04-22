#Shapes
import turtle
#imports the turtle library

mike=turtle.Turtle()
leo=turtle.Turtle()
raph=turtle.Turtle()
don=turtle.Turtle()
#creates an instance of the Class Turtle
leo.color("blue")
leo.shape("turtle")
leo.penup()
leo.goto(200,200)
leo.pendown()

mike.color("orange")
mike.shape("turtle")
mike.penup()
mike.goto(-200,-200)
mike.pendown()

raph.color("red")
raph.shape("turtle")
raph.penup()
raph.goto(-200,200)
raph.pendown()

don.color("purple")
don.shape("turtle")
don.penup()
don.goto(200,-200)
don.pendown()

mike.begin_fill()
for m in range(0,10):
    mike.forward(100)
    if m%2 == 0:
        mike.right(175)
    else:
        mike.left(255)
mike.end_fill()

leo.begin_fill()
for l in range(0,4):
    leo.forward(90)
    leo.right(90)
leo.end_fill()

raph.begin_fill()
for r in range (0,6):
    raph.forward(90)
    raph.right(60)
raph.end_fill()

don.begin_fill()
for d in range (0,3):
    don.forward(60)
    don.right(120)
don.end_fill()
    

