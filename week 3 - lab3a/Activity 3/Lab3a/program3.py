from math import *

# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “We have not given or received any unauthorized aid on this assignment”
# Names:          Connor Tisdel 627004745
#                 Chance Smith 727001732
#                 Arya Ramchandani 627007018
#                 Alvin Yolanda Ewaldo 227008703
# Section:        021
# Assignment:     Lab03a - 3
# Date:           11 September 2018

print("\n***The story you\'re about to enter will go like this.\nThe hero named \"\t\t\" at the \nage of \"\t\t\" will head to \"\t\t\" along \nwith \"\t\t\" to discover the lost \"\t\t\" treasure.")
print("The legendary lost \"\t\t\" treasure is guarded by the feared,")
print("undead pirate, Dreadbeard. \"\t\t\" realizes upon arrival that he should have \nbeen more careful with who he trusted, \nas \"\t\t\" stabbed him through the heart.\n")
print("***You will fill in the missing quotes\nin order to complete the story.\n")

inputName = input("Enter name below:\n")
inputAge = int(input("Enter the age of \""+inputName+"\" below:\n"))
inputLoc = input("Enter location below:\n")
inputSide = input("Enter "+inputName+"\'s companion below:\n")
inputObj = input("Enter the treasure they\'re looking for below:\n")

print("\nThe hero named "+inputName+" at the \nage of "+str(inputAge)+" will head to "+inputLoc+" along \nwith "+inputSide+" to discover the lost "+inputObj+" treasure.")
print("The legendary lost",inputObj,"treasure is guarded by the feared,")
print("undead pirate, Dreadbeard.",inputName,"realizes upon arrival that he should have \nbeen more careful with who he trusted, \nas",inputSide," stabbed him through the heart.")