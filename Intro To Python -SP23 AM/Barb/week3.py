#Dungeons And Dragons!
#

beginningStory="In the land of Pythonia, a small group of data traveled through Microsoftia Forest.When they reached the forest's edge they found a cave..."
choice1=" 1. go in the cave, "
choice2=" 2. find a way around the cave, "
choice3=" 3. blow up the cave with dynamite"

print(beginningStory)
print("The Data can either: " + choice1 + choice2 + choice3 )

caveAction=input("What do you think the data should do? Enter the number of your choice.")

#print(caveAction)
if caveAction=="1":
    print("The data enters the cave... and....")
elif caveAction=="2":
    print("The data looks for a way around the cave...")
elif caveAction=="3":
    print("They all get blown up!")
else:
    print("You did not enter the choice correctly.")


    







