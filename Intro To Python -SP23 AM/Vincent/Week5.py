#april fools LOL OMG XYZ
import turtle
wn=turtle.Screen()
img="maze.gif"
wn.bgpic(img)
def Funct(parameter):
    pass

def turnleft():
    player.left(90)

def turnright():
    player.right(90)

def goforward():
    player.forward(10)

def goback():
    player.forward(-10)


player=turtle.Turtle()
player.shape("turtle")
turtle.listen()
turtle.onkey(turnleft,"Left")
turtle.onkey(turnright,"Right")
turtle.onkey(goforward,"Up")
turtle.onkey(goback,"Down")
player.color("red")
#player.forward(200)
#turnleft(player)
