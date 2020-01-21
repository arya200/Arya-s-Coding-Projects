# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Names:          Kyle Loshelder  |927007957
#                 Vedik Jayaraj   |927005523
#                 Zixuan Jia      |227006636
#                 Karim Zaher     |327004766
# Section:        020
# Assignment:     Lab 12a
# Date:           12 November 2018

#*************************************************
# NOTICE: when converging to 10^-6, the program
#         takes a very, very, very long time to
#         execute.
#         In order to change it to something
#         faster such as ^-2, the following lines
#         need to be changed:
#           line: 58
#           line: 81
#           line: 106
#           line: 131
# ************************************************

from math import *


def f(coefficients, x=0):
   '''takes the coefficients of a polynomial, and an x value, and returns f(x)'''
   y = 0
   for i in range(len(coefficients)):
       y += coefficients[i] * (x**i)
   return y

def areaRect(length, width):
    return length*width

def areaTrap(a, b, h):
    return ((a+b)/2)*h

def fAreaBeginning(coefficients, start, end):
    withinTolerance = False
    iterations = 0
    subsections = 10
    area = 0
    # calculate area when subsections = 10
    interval = (end-start)/subsections
    for i in range(subsections):
        area += areaRect(interval, f(coefficients, start + i*interval))
    while withinTolerance == False:
        subsections *= 10
        interval = (end-start)/subsections
        nextArea = 0
        for i in range(subsections):
            nextArea += areaRect(interval, f(coefficients, start + i * interval))


        area = nextArea
        iterations += 1

    return round(area, 6), iterations

def fAreaEnd(coefficients, start, end):
    withinTolerance = False
    iterations = 1
    subsections = 10
    area = 0
    # calculate area when subsections = 10
    interval = (end - start) / subsections
    for i in range(1, subsections+1):
        area += areaRect(interval, f(coefficients, start + i * interval))
    while True:
        subsections *= 10
        interval = (end - start) / subsections
        nextArea = 0
        for i in range(subsections):
            nextArea += areaRect(interval, f(coefficients, start + i * interval))
        # if calculation is within 10**-6 of the previous calculation


        area = nextArea
        iterations += 1

def fAreaMid(coefficients, start, end):
    withinTolerance = False
    iterations = 1
    subsections = 10
    area = 0
    # calculate area when subsections = 10
    interval = (end - start) / subsections
    for i in range(0, subsections):
        endPoint = start + (i+1)*interval
        startPoint = start + i*interval
        area += areaRect(interval, f(coefficients, (endPoint + startPoint)/2))
    while True:
        subsections *= 10
        interval = (end - start) / subsections
        nextArea = 0
        for i in range(subsections):
            endPoint = start + (i + 1) * interval
            startPoint = start + i * interval
            nextArea += areaRect(interval, f(coefficients, (endPoint + startPoint) / 2))
        # if calculation is within 10**-6 of the previous calculation


        area = nextArea
        iterations += 1

def fAreaTrap(coefficients, start, end):
    withinTolerance = False
    iterations = 1
    subsections = 10
    area = 0
    # calculate area when subsections = 10
    interval = (end - start) / subsections
    for i in range(0, subsections):
        endPoint = start + (i + 1) * interval
        startPoint = start + i * interval
        area += areaTrap(f(coefficients, startPoint), f(coefficients, startPoint), interval)
    while True:
        subsections *= 10
        interval = (end - start) / subsections
        nextArea = 0
        for i in range(subsections):
            endPoint = start + (i + 1) * interval
            startPoint = start + i * interval
            nextArea += areaTrap(f(coefficients, startPoint), f(coefficients, startPoint), interval)
        # if calculation is within 10**-6 of the previous calculation


        area = nextArea
        iterations += 1

# f(x) = 3x^2 + 4x  on an interval of [-10, 10]
coeff = [0,4,3]

print("Calculating the area under the function 3x^2 + 4x on the interval [0, 10]: ")

ans = fAreaBeginning(coeff, -10, 10)
print("A rectangle whose height is the value of the function at the beginning of the interval gave the answer", ans[0], "after", ans[1], "iterations")

ans = fAreaEnd(coeff, -10, 10)
print("A rectangle whose height is the value of the function at the end of the interval gave the answer", ans[0], "after", ans[1], "iterations")

ans = fAreaMid(coeff, -10, 10)
print("A rectangle whose height is the value of the function at the midpoint of the interval gave the answer", ans[0], "after", ans[1], "iterations")

ans = fAreaTrap(coeff, -10, 10)
print("A trapezoid with one parallel edge being the value of the function at the beginning of the interval, and another being the value of the function at the end of the interval", ans[0], "after", ans[1], "iterations")

