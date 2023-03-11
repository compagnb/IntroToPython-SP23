# Week 2 - Basic AI

print("Hi there, my name is Glitch, and i am a rogue A.I.")
name = input("What is your name")
helloSentence = " your name is " +name+ " it's nice to meet you!"
print (helloSentence)
age = input("How old are you?")
yearsToDrive = 16-int(age)
driveSentence = "ur " +age+ "  years left until u can drive." +str(yearsToDrive)
print (driveSentence)
currentYear= input("What is the current year?")
yearAbleToDrive = int(currentYear)+yearsToDrive
print("I hope I'm not on then road in "+str (yearAbleToDrive) +" because someone's going to be driving not me!")
