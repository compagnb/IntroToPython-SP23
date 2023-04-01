#April Fool's Day!
import turtle #imports the module turtle

#Functions!!
def myFunction(parameter):
   pass

def turnLeft():
    player.right(30)
def turnRight():
    player.left(30)
def goForward():
    player.backward(10)
def goBack():
    player.forward(10)
    

player = turtle.Turtle()#stores an object of the class Turtle in our variable

player.shape("turtle")
player.color("red")

turtle.listen()
turtle.onkey(turnLeft, "Left")
turtle.onkey(turnRight, "Right")
turtle.onkey(goForward, "Up")
turtle.onkey(goBack, "Down")
            

#player.forward(100)
#player.right(90)
#player.backward(200)
#player.left(30)
#turnLeft(player)
