#Dungeons And Dragons

beginningStory="In the land of Broccolia, a small group of sprouts traveled through The Stemming Forest. When they reached the edge of the forest they found a cave..."

choice1="1.Go in the cave, "
choice2=" 2.Find a way around, "
choice3=" 3.Blow the cave up with buds, "

print(beginningStory)
print("The sprouts can either: " + choice1 + choice2+ choice3)

caveAction=input ("What should the sprouts do? Enter the number of your choice.")

#print(caveAction)
if caveAction=="1":
    print("The sprouts entered the cave... and... they find a large dragon in the cave.")
elif caveAction=="2":
    print("The sprouts looked around for a way around the cave")
elif caveAction=="3":
    print("The sprouts blow up the cave, but in doing so, they blow themselves up.")
else:
    print("You did not enter a valid option.")
