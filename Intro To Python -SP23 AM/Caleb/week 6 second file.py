#shapes
import turtle
leo=turtle.Turtle()
leo.color("blue")
leo.shape("turtle")
leo.penup()
leo.goto(200,200)
leo.pendown()
for i in range (0,4):
    leo.forward(100)
    leo.right(90)

mike=turtle.Turtle()
mike.color("red")
mike.shape("turtle")
mike.begin_fill()
for i in range(0,19):
    mike.forward(100)
    if i%2 == 0:
        mike.right(175)
    else:
        mike.left(255)
mike.end_fill()

###Shapes
##import turtle #imports the turtle
##
##mike=turtle.Turtle() #creates an instance of the Class Turtle
##
##mike.color("red")
##mike.shape("turtle")
##mike.begin_fill()
##for i in range(0,9):
##    if i%2 == 0
##    mike.forward(40)
##    mike.right(40)
##    else:
##    mike.end_fill()
##    
##    

import turtle
raph=turtle.Turtle ()
raph.color("green")
raph.shape("turtle")
raph.penup()
raph.goto(-200,-200)
raph.pendown()
for i in range (0,9):
    raph.forward(40)
    raph.right(40)

import turtle
ryu=turtle.Turtle()
ryu.color("purple")
ryu.shape("turtle")
ryu.penup()
ryu.goto(-100,-100) 
ryu.pendown()
for i in range(0,3):
    ryu.forward(60)
    ryu.right(120)





