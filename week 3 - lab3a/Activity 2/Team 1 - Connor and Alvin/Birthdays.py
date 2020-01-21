# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Names:          Connor Tisdel 627004745
#                 Alvin Yolanda Ewaldo 227008703
# Section:        021
# Assignment:     Lab03 - 1
# Date:           10 September 2018

Name_One = input("Enter your first name: ")
Name_Two = input("Enter your first name: ")
Name_Three = input("Enter your first name: ")
Name_Four = input("Enter your first name: ")

Birthday_One = input("Enter " + str(Name_One) + "'s birthday (MM/DD/YYYY): ")
Birthday_Two = input("Enter " + str(Name_Two) + "'s birthday (MM/DD/YYYY): ")
Birthday_Three = input("Enter " + str(Name_Three) + "'s birthday (MM/DD/YYYY): ")
Birthday_Four = input("Enter " + str(Name_Four) + "'s birthday (MM/DD/YYYY): ")

print("-------------------------------")
print(str(Name_One).ljust(10) + str(Birthday_One).rjust(20))
print(str(Name_Two).ljust(10) + str(Birthday_Two).rjust(20))
print(str(Name_Three).ljust(10) + str(Birthday_Three).rjust(20))
print(str(Name_Four).ljust(10) + str(Birthday_Four).rjust(20))