#Shapes
import turtle
#imports the turtle library
leo=turtle.Turtle()
#creates an instance of the Class Turtle
leo.color("blue")
leo.shape("turtle")
leo.penup()
leo.goto(200,200)
leo.pendown()
for i in range(0,4):
    leo.forward(100)
    leo.right(90)

raph=turtle.Turtle()
#creates an instance of the Class Turtle
raph.color("red")
raph.shape("turtle")

don=turtle.Turtle()
#creates an instance of the Class Turtle
don.color("purple")
don.shape("turtle")

mike=turtle.Turtle()
#creates an instance of the Class Turtle
mike.color("orange")
mike.shape("turtle")

mike.begin_fill()
for i in range(0,19):
    mike.forward(100)
    if i%2 == 0:
        mike.right(175)
    else:
        mike.left(255)
mike.end_fill()




