# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “We have not given or received any unauthorized aid on this assignment”
#
# Names:          Arya Ramchandani 627007018
#
# Section:        021
# Assignment:     Lab08b - 1b
# Date:           24 October 2018

def velocity(time, distance):

    avg_velocity = []
    for i in range(len(time)):
        avg = (distance[i] + distance[i+1])/(time[i] + time[i+1])

        avg_velocity += [avg]

    return avg_velocity