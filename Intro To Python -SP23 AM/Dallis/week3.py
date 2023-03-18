#Dungeons and Dragons!

beginningStory= "In the land of Espera, a small group of adventurers traveled the forest in hope of a good time. When they reached the end of the forest, they reached a palace..."
choice1 = "A.go inside blindly,"
choice2 = "B.look for the owner,"
choice3 = "C.or look through the window"
print(beginningStory)
print("The adventurers can either:" + choice1 + choice2 + choice3)
palaceAction=input("What do you think the adventurers should do? Enter the letter or your choice.")
#print(PalaceAction)
if palaceAction == "A":
    print("The adventurers went into the palace without a care in the world")
elif palaceAction== "B":
    print ("The adventurers searched for the owner.")
elif palaceAction == "C":
    print("The adventurers look through the window.")
else:
    print ("What do you mean by '" + palaceAction + "'?")
    
