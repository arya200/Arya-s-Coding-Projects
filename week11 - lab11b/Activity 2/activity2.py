# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “We have not given or received any unauthorized aid on this assignment”
#
# Names:          Arya Ramchandani 627007018
#
# Section:        021
# Assignment:     Lab08b - 1b
# Date:           24 October 2018

from math import *


def volume(height, length, width, radius):

    v_of_cylinder = pi * (radius**2) * height

    v_of_box = length * height * width

    volume_remaining = v_of_box - v_of_cylinder

    print("The volume remaining is: ", volume_remaining )


height = float(input("Enter the height: "))
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
radius = float(input("Enter the radius: "))

volume(height,length,width,radius)








