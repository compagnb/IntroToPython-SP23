#yu
import random
hilimit=10
lowlimit=1
ans=random.randint(lowlimit, hilimit)
guess=input("Guess a number between "+str(lowlimit)+" and "+str(hilimit))
print(guess)
if int(guess) == ans:
    print("GG, you win")
else:
    print("Have another try")
    g2=input("Guess a number between "+str(lowlimit)+" and "+str(hilimit)
             )
    print(g2)
    if int(g2) == ans:
        print("GG, you win")
    else:
        print("Last try...")
        g3=input("Guess a number between "+str(lowlimit)+" and "+str(hilimit))
        print(g3)
        if int(g3) == ans:
            print("GG, you win")
        else:
            print("You lose, wamp wamp waaa")
