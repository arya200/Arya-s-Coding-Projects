# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:           Arya Ramchandani
# Section:        021
# Assignment:     lab6b-1
# Date:           10/3/18

import math
from math import *

check=0
avg = 0
maximum=0
minimum = 100**100
print("This program will use the numbers entered in order to find the maximum minimum and average number")


while True:
    check+=1
    value = float(input("Enter a number: "))


    if(value<0):
        print("The maximum is: ", maximum)
        print("The minimum is: ", minimum)
        print("The average is:", avg)
        break

    if(value>=0):

        avg = avg + value
        final_avg = avg/check

        if(value > maximum):
            maximum = value

        if(value < minimum):
            minimum = value

    print("The maximum is: ", maximum)
    print("The minimum is: ", minimum)
    print("The average is:", final_avg)