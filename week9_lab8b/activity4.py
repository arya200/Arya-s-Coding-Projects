# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “We have not given or received any unauthorized aid on this assignment”
#
# Names:          Arya Ramchandani 627007018
#
# Section:        021
# Assignment:     Lab08b - 4
# Date:           24 October 2018

import statistics
import csv
humidity_count=0
t_high=0
t_low=0
low_temp=[]
avg_temp=[]
monthly_high=[]
humidity=[]
avg_precipitation=0
sum_precipitation = 0
hum_average = 0

sum_t = 0
with open('WeatherDataWindows.csv', 'r') as csv_file:
    temp = csv.reader(csv_file)


    next(temp)

    for i in temp:

        # humidity
        hum_a = float(i[8])
        humidity.append(hum_a)
        if hum_average >= 90:
            humidity_count += 1

        # high temp avg for April
        sum_t = float(i[1])
        monthly_high.append(sum_t)
        mon_high = monthly_high[92:123]

        # average of precipitation
        sum_precipitation += (float(i[13]))
        avg_temp.append(avg_precipitation)
        avg_precipitation = sum_precipitation / len(avg_temp)

        # find the maximum
        maximum = float((i)[1])
        high_temp = max(t_high,maximum)

        # find the minimum
        minimum = float((i)[2])
        low_temp = max(t_low, minimum)
        low_temp.append(low_temp)

    print('The maximum temperature in three years is ',t_high)
    print ('The minimum temperature in three years is ',min(low_temp))

    # average of precipitation
    print('The average daily precipitation ',avg_precipitation)


    print ('The average high temperature for April is ',sum(monthly_high)/30)


    print('There are ',(len(humidity)- humidity_count)/len(humidity)*100,'%',' of days that the humidity was below 90%')
    print('There are ', humidity_count / len(humidity) * 100, '%', 'of days that the humidity was below 90%')

    # precipitation standard deviation

    print ('The mean of the precipitation level is ', avg_precipitation, 'The standard deviation of the precipitation is ', statistics.stdev(avg_temp))
