#Shapes
import turtle #imports the turtle library
broccoli=turtle.Turtle() #creates an instance of the class turtle

broccoli.color("green")
broccoli.shape("circle")
broccoli.begin_fill()
for i in range(0,360):
    broccoli.forward(1)
    broccoli.right(1)
broccoli.end_fill()
broccoli.color("yellow")
broccoli.begin_fill()
for i in range(0,10):
    broccoli.forward(90)
    broccoli.left(38.38)
broccoli.end_fill()
broccoli.color("blue")
for i in range(0,27):
    broccoli.forward(47)
    broccoli.left(29.3)
broccoli.color("purple")
for i in range(0,90):
    broccoli.forward(46)
    broccoli.right(73.256)

