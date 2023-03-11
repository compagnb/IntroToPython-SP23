# Week 2 - Basic AI

print("Hi my name is HAL, and I am an AI.")
name = input("What is your name?")
helloSentence = "Hi " +name+ "! it's nice to meet you!"
print(helloSentence)
age = input("How old are you?")
yearsToDrive = 16-int(age)
driveSentence = "Oh, you are " +age+" years old, only " +str(yearsToDrive)+ " until you can drive."
print(driveSentence)
currentYear= input("What is the current year?")
yearAbleToDrive = int(currentYear)+yearsToDrive
print("I hope I'm not on the road in "+str(yearAbleToDrive) +" because you will be driving!")
