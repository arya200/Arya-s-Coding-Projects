# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:           Arya Ramchandani
# Section:        021
# Assignment:     lab6b-1
# Date:           10/3/18

for x in range(2,101):
   for y in range(2,101):
       if x%y == 0:
           print(y, "divides" , x)
