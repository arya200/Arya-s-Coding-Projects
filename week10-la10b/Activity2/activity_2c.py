
# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “We have not given or received any unauthorized aid on this assignment”
#
# Names:          Arya Ramchandani 627007018
#
# Section:        021
# Assignment:     Lab10-2c
# Date:           4 November 2018

import csv
import matplotlib.pyplot as plt

avg_temp = []
avg_dew_point = []

with open('WeatherDataWindows.csv', 'r') as csv_file:
    temp = csv.reader(csv_file)


    next(temp)

    for i in temp:

        avg_temp += [float(i[2])]
        avg_dew_point += [float(i[5])]


plt.scatter(avg_temp, avg_dew_point, label= 'average dew points')
plt.xlabel('average temperature')
plt.ylabel('average dew point')
plt.legend(loc='upper left')
plt.title('Average temperature vs Average dew point')
plt.show()