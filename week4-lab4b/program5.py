# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:           Arya Ramchandani
# Section:        021
# Assignment:     lab4b-5
# Date:           23/9/18

from math import *

print("This program is meant to find the roots for a given quadratic equation(ax2+bx+c) they exist")


print("Input the first coefficient  of the quadratic equation, i.e 'a' the coefficient to x^2 ")

a = float(input())

print("Input the second coefficient of the quadratic equation, i.e 'b' the coefficient to x ")

b = float(input())

print("Input the third coefficient of the quadratic equation, i.e 'c' ")

c = float(input())
d = ((b ** 2) - (4 * a * c))

if((a==0) and  (b==0) and (c==0)):
    print("All coefficients entered were zero, infinite roots, please re run the program")

elif((a==0) and (b==0)):
    print("This function has no roots")

elif(a==0):
    print("This is a linear function")
    if(c<0):
        root1 = abs(c)/b
        print("The root is:", root1)
    elif(c>0):
        root1 = -(c/b)
        print("The root is:", root1)





else:


    if(d<0):

        root1 = str(-b/(2*a)) + "+" + str(sqrt(abs(d))/(2*a))+ "i"
        root2 = str(-b/(2*a)) + "-" + str(sqrt(abs(d))/(2*a))+ "i"
        print("This equation has 2 imaginary roots:", root1, "&", root2)

    elif(d==0):

        root1 = ((-b + (sqrt(d))) / (2 * a))
        print("This equation has one root: ", root1)

    elif(d>0):
        root1 = ((-b + (sqrt(d))) / (2 * a))
        root2 = ((-b - (sqrt(d))) / (2 * a))
        print("This equation has two roots: ", root1, "&", root2)



