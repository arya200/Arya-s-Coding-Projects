# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “We have not given or received any unauthorized aid on this assignment”
#
# Names:          Arya Ramchandani 627007018
#
# Section:        021
# Assignment:     Lab08b - 1b
# Date:           24 October 2018

def properties(values):

    maximum = max(values)
    minimum = min(values)
    sumation = sum(values)
    mean = sumation/(len(values))

    return maximum, minimum, mean

