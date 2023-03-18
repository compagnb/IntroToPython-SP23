#Dungeons And Dragons
#


beginningStory="In the land of Blue Hills, a small group of Heroes traveled trough truffman forest. When they reached the truffman's edge when they found a cave..."
choice1=" 1. go in the cave"
choice2=" 2. find a way around the cave"
choice3=" 3. blow up the cave with dynamite"

print(beginningStory)
print("the heroes can either: " + choice1 + choice2 + choice3 )

caveAction=input("What do you think the heroes should do? Enter the number of your choice.")

#print(caveAction)
if  caveAction=="1":
     print("the data enters the cave...and....")
elif caveAction=="2":
     print("The heroes look for a way around the cave...")
elif caveAction=="3":
     print("The group heroes hear a noise from the cave...3 of them decide to set up the explosives but right as they blow it up,a hero named Redhead went in last second ")
else:
     print:("You did not pick the choice  correctly")
