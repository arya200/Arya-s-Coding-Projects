# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:           Arya Ramchandani
# Section:        021
# Assignment:     lab4b-4
# Date:           23/9/18

print("Enter the number of days to find out how many widgets were produced: ")

days = float(input())

if(days <= 10):
    widgets = days * 10
    print("It will produce:", widgets, "widgets")

elif(11<= days <=60):
    widgets = 100 + ((days-10) * 40)
    print("It will produce:", widgets, "widgets")

elif(61 <= days <= 100):
    widgets = 2100 + (((days-60)/2)*((2*39)+((days-61)*-1)))
    print("It will produce:", widgets, "widgets")


else:
    print("It will produce 0 widgets ")