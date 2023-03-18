#Mario's Cave Adventure
#

beginingStory="In the Mushroom Kingdom, a Mario traveled through The Mushroom Forest. When he reached the forest's edge he found a cave..."
choice1= "1. flee like a cowardly baby, "
choice2= "2. BLOW UP THE CAVE WITH DYNAMITE!!!!!!! "
choice3= "3. go in the cave like a manly BBBBBOOOOOYYYYY!!!!! "

print (beginingStory)
print ("Mario can either: " +choice1 + choice2 +choice3 )

caveAction=input("What do you think Mario should do? Enter the number of your choice.")

#print (caveAction)
if caveAction=="1":
    print("Mario is a coward! LOL LOL LOL LOL LOL! GAME OVER!")
if caveAction =="2":
    print("Mario dies because he accedently blew himself up in the proccess")
if caveAction =="3":
    print ("Mario sees Bowser in the cave and beats him up! Mario has restored peace to the Mushroom Kingdom, and the adventure is-a-done!")
