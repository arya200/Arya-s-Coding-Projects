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


def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)


t1 = np.arange(0.25, 3.0, 0.11)


t2 = np.arange(0.5, 7.0, 0.375)

plt.figure(1)
plt.subplot(211)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')
plt.xlabel('kids')
plt.ylabel("adults")



plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')

plt.xlabel("kids")
plt.ylabel("adults")
plt.show()