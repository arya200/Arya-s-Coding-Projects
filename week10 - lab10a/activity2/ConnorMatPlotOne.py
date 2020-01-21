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
import matplotlib.pyplot as plt
import numpy as np

data = {'a': np.arange(50),
        'c': np.random.randint(0, 200, 50),
        'd': np.random.randn(50)}
data['b'] = data['a'] + 35 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 75

plt.scatter('a', 'b', c='c', s='d', data=data)
plt.suptitle('A Very Interesting Title')
plt.xlabel('Number of Days Since the Start of the Semester')
plt.ylabel("Number of Times Students Interrupt Dr. Koola's Class")
plt.show()