#Solar System
import turtle
wn = turtle.Screen()
wn.tracer(3)
sun=turtle.Turtle()
sun.color("yellow")
sun.shape("circle")
import turtle
planet1=turtle.Turtle()
import turtle
planet2=turtle.Turtle()
import turtle
planet3=turtle.Turtle()
planet1.shape("circle")
planet1.penup()
planet1.forward(55)
planet1.left(90)
planet1.pendown()
planet2.shape("circle")
planet2.penup()
planet2.forward(100)
planet2.left(90)
planet2.pendown()
planet3.shape("circle")
planet3.penup()
planet3.forward(150)
planet3.right(90)
planet3.pendown()
for i in range(0,99999999999):
    planet1.forward(1)
    planet1.left(1)
    planet2.forward(1)
    planet2.left(0.5)
    planet3.forward(1)
    planet3.right(0.275)
    
