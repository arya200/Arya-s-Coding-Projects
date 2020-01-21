# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Names:          Arya Ramchandani 627007018
# Section:        021
# Assignment:     Lab 10-1
# Date:           4 November 2018

import numpy as np
import matplotlib.pyplot as plt

x = np.array([])
y = np.array([])

v = np.matrix([1,0]).reshape(2,1)

M = np.matrix([(1.00583,-0.087156) , (0.087156,1.00583)])

for i in range(200):
   v1 = M@v
   v = v1
   x = np.append(x,v1[0])
   y = np.append(y,v1[1])

plt.plot(x,y)
plt.xlabel('x values')
plt.ylabel('y values')
plt.suptitle('A spiral is created by repeatedly multiplying the matrix and the vector ')
plt.show()






