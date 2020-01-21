
# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “We have not given or received any unauthorized aid on this assignment”
#
# Names:          Arya Ramchandani 627007018
#
# Section:        021
# Assignment:     Lab10 - 2b
# Date:           4 November 2018

import csv
import matplotlib.pyplot as plt

date = []
precipitation = []

with open('WeatherDataWindows.csv', 'r') as csv_file:
    temp = csv.reader(csv_file)


    next(temp)

    for i in temp:

        date += [(i[0])]
        precipitation += [float(i[13])]

bins = []
for k in range(9):
    bins += [k]

plt.xlabel("Precipitation")
plt.ylabel("Days")
plt.title('Precipitation vs days')
plt.hist(precipitation, bins, histtype="stepfilled", rwidth=0.5, label= 'Precipitation')
plt.legend(loc='upper right')
plt.show()
