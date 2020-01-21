# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “We have not given or received any unauthorized aid on this assignment”
#
# Names:          Connor Tisdel 627004745
#                 Chance Smith 727001732
#                 Arya Ramchandani 627007018
#                 Alvin Yolanda Ewaldo 227008703
# Section:        021
# Assignment:     Lab 10A-1
# Date:           30 October 2018

import numpy as np
import matplotlib.pyplot as plt

plt.title('I Love This Title')
line_up, = plt.plot([.5,2,3],[3,6,15], label='Fortnite')
line_down, = plt.plot([0,2,3],[4,3,2.5], label='PUBG')
plt.legend(handles=[line_up, line_down])

plt.ylabel('Sales')
plt.xlabel('Time')
plt.show()