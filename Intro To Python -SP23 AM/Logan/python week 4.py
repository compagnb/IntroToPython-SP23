#Guessing Game
import random  #importing the random module

# hereb are the variables for limits
hiLimit=10
lowLimit=1

# here is the answer variable
ans=random.randint(lowLimit, hiLimit)

# here is the variable that stores the users guess
guess=input("Guess what number I am, thinking of between "+str(lowLimit)+" and"+str(hiLimit)+".")

if int (guess) == ans:
    print("You are .... CORRECT!!")
else:
    print("you are.......WRONG")
