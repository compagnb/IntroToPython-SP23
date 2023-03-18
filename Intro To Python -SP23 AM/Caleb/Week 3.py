#Dungeons and Dragons!
#

beginningStory="In the land of Pythonia, a small group of data traveled through Microsoftia Forest. When they reachhed the forest's edge they found a cave..."

choice1=" 1.Go in the cave, "
choice2=" 2.Batte the beast, "
choice3=" 3.Eat a baked potato and a carrot"
print(beginningStory)
print("the data can either: " + choice1 + choice2 +choice3 )

caveAction=input("What do you think the data should do? Enter the number of your choice.")

#print(caveAction)
if caveAction=="1":
    print("The data enters the cave... and...")
elif caveAction=="2":
    print("the data looks for a way around the cave...")
elif caveAction=="3":
    print("they all get blown up!")
else:
    print("You did not enter the choice correctly.")
