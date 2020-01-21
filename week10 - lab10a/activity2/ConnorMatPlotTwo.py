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

names = ['Connor', 'Chance', 'Alvin']
values = [0, 25, 35]

plt.figure(3, figsize=(15, 5))

plt.subplot(162)
plt.bar(names, values)
plt.xlabel('Different People')
plt.ylabel('Number of Times Rejected In 1 Day')
plt.subplot(164)
plt.xlabel('Different People')
plt.ylabel('Number of Times Rejected In 1 Day')
plt.scatter(names, values)
plt.subplot(166)
plt.plot(names, values)
plt.suptitle('Categorical Plotting')
plt.xlabel('Different People')
plt.ylabel('Number of Times Rejected In 1 Day')
plt.show()

