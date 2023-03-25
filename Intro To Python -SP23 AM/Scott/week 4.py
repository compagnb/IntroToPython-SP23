#Guessing Game
import random

# here are the variables for limits
hiLimit=10
lowLimit=1

# here is the answer variable
ans=3

# here is the variable that stores the users guess

guess=input("Guess what number I am thinking of between "+str (1)+str (10)
if int(guess) == ans:
    print("correct!!")
else:
    print("you are wrong")
    print("you have 2 more chances")
    guess=input("Guess what number I am thinking of between 1 and 10")
    if int(guess) == ans:
        print("correct!!")
    else:
        print("you have 1 more chance")
        guess=input("Guess what number I am thinking of between 1 and 10")
        if int(guess) == ans:
            print("correct!!")
        else:
            print("you have 0 more chances, you lost")
