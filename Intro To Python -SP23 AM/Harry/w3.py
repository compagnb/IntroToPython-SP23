#Dungeons And DRAGONS!
#

beginningstory="In the land of Pythoni, a small group of data traveled through Mincrosftia Forest. When they reach the forest's edge they found a cave..."
choice1=" 1. go in the cave,"
choice2=" 2. find a way around the cave,"
choice3=" 3. blow up the cave with dynamite"

print(beginningstory)
print("The Data can either: " + choice1 + choice2 + choice3 )

CaveAction=input("What do you think the data schould do? Enter the number of your choice.")

#print(caveAction)
if CaveAction=="1":
    print("The data enters the cave... and....")
elif CaveAction=="2":
    print("They find a way around")
elif CaveAction=="3":
    print("POW!!!")
else:
    print("you did not enter the choice correctly.")  
