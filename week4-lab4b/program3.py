# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:           Arya Ramchandani
# Section:        021
# Assignment:     lab4b-3
# Date:           23/9/18
print("Please enter the kinematic velocity: ")
viscosity = float(input())

print("Please enter the fluid velocity: ")
velocity = float(input())

print("Please enter the characteristic linear dimension: ")
dimension = float(input())

reynolds_number = ((velocity*dimension)/viscosity)

if(reynolds_number < 2300):
    print("The flow is laminar")

elif (2300 <= reynolds_number <= 4000):
    print("The flow is transient")

elif(reynolds_number > 4000):
    print("The flow is turbulent")







