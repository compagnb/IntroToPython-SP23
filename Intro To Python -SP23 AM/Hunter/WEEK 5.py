#April Fool's Day!

import turtle #imports the module turtle
turtle.speed(0)
#Functions!!
def myFunction(parameter):
    pass

def turnLeft():
    player.left(30)

def turnRight():
    player.right(30)

def goForward():
    player.forward(100)

def goBackward():
    player.backward(100)



player=turtle.Turtle()
#stores an object of the class Turtle in our player variable

player.shape("square")
player.color("blue")

turtle.listen()
turtle.onkey(turnLeft,"Left")
turtle.onkey(turnRight,"Right")
turtle.onkey(goBackward,"Down")
turtle.onkey(goForward,"Up")


#player.forward(100)
#player.backward(200)
#player.left(30)
#player.right(90)
#turnLeft(player)


