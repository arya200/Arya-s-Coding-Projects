# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “We have not given or received any unauthorized aid on this assignment”
#
# Names:          Arya Ramchandani 627007018
#
# Section:        021
# Assignment:     Lab10b - 2a
# Date:           4 November 2018

import matplotlib.pyplot as plt
import csv

date = []
avg_temp = []
pressure = []

sum_t = 0
with open('WeatherDataWindows.csv', 'r') as csv_file:
    temp = csv.reader(csv_file)


    next(temp)

    for i in temp:

        date += [i[0]]
        avg_temp += [float(i[2])]
        pressure += [float(i[11])]

fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('date')
ax1.set_ylabel('Average temperature', color=color)
ax1.plot(date, avg_temp, color=color, label = 'Average Temperature')
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:blue'
ax2.set_ylabel('Pressure', color=color)  # we already handled the x-label with ax1
ax2.plot(date, pressure, color=color, label = 'Pressure')
ax2.tick_params(axis='y', labelcolor=color)
ax1.legend()
ax2.legend()

plt.title('Pressure and Temperature vs Dates')
plt.show()