
# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “We have not given or received any unauthorized aid on this assignment”
#
# Names:          Arya Ramchandani 627007018
#
# Section:        021
# Assignment:     Lab10-2d
# Date:           4 November 2018

import csv
import matplotlib.pyplot as plt

date = []
avg_temp = []
avg_dew = []
final_values = []
temp_high = []
temp_low = []
low_days = []
high_days = []

with open('WeatherDataWindows.csv', 'r') as csv_file:
    temp = csv.reader(csv_file)

    next(temp)  # skip the heading

    for i in temp:

        high_days += [i[1]]
        low_days += [i[3]]
        avg_temp += [float(i[2])]

        # Jan 2015

        monthly_temp_sum1 = sum(avg_temp[0:31])
        avg_temp1 = monthly_temp_sum1 / 31

        # Feb 2015
        monthly_temp_sum2 = sum(avg_temp[31:59])
        avg_temp2 = monthly_temp_sum2 / 28

        # March 2015
        monthly_temp_sum3 = sum(avg_temp[59:90])
        avg_temp3 = monthly_temp_sum3 / 31

        # April 2015
        monthly_temp_sum4 = sum(avg_temp[90:120])
        avg_temp4 = monthly_temp_sum4 / 30

        # May 2015
        monthly_temp_sum5 = sum(avg_temp[120:151])
        avg_temp5 = monthly_temp_sum5 / 31

        # June 2015
        monthly_temp_sum6 = sum(avg_temp[151:180])
        avg_temp6 = monthly_temp_sum6 / 30

        # July 2015
        monthly_temp_sum7 = sum(avg_temp[180:211])
        avg_temp7 = monthly_temp_sum7 / 31

        # August 2015
        monthly_temp_sum8 = sum(avg_temp[211:242])
        avg_temp8 = monthly_temp_sum8 / 31

        # September 2015
        monthly_temp_sum9 = sum(avg_temp[242:272])
        avg_temp9 = monthly_temp_sum9 / 30

        # October 2015
        monthly_temp_sum10 = sum(avg_temp[272:303])
        avg_temp10 = monthly_temp_sum10 / 31

        # November 2015
        monthly_temp_sum11 = sum(avg_temp[303:333])
        avg_temp11 = monthly_temp_sum11 / 30

        # December 2015
        monthly_temp_sum12 = sum(avg_temp[333:364])
        avg_temp12 = monthly_temp_sum12 / 31

        # Jan 2016
        monthly_temp_sum1_16 = sum(avg_temp[364:395])
        avg_temp1_16 = monthly_temp_sum1_16 / 31

        # Feb 2016
        monthly_temp_sum2_16 = sum(avg_temp[395:424])
        avg_temp2_16 = monthly_temp_sum2_16 / 28

        # March 2016
        monthly_temp_sum3_16 = sum(avg_temp[424:455])
        avg_temp3_16 = monthly_temp_sum3_16 / 31

        # April 2016
        monthly_temp_sum4_16 = sum(avg_temp[455:485])
        avg_temp4_16 = monthly_temp_sum4_16 / 30

        # May 2016
        monthly_temp_sum5_16 = sum(avg_temp[485:516])
        avg_temp5_16 = monthly_temp_sum5_16 / 31

        # June 2016
        monthly_temp_sum6_16 = sum(avg_temp[516:546])
        avg_temp6_16 = monthly_temp_sum6_16 / 30

        # July 2016
        monthly_temp_sum7_16 = sum(avg_temp[546:577])
        avg_temp7_16 = monthly_temp_sum7_16 / 31

        # August 2016
        monthly_temp_sum8_16 = sum(avg_temp[577:608])
        avg_temp8_16 = monthly_temp_sum8_16 / 31

        # September 2016
        monthly_temp_sum9_16 = sum(avg_temp[608:638])
        avg_temp9_16 = monthly_temp_sum9_16 / 30

        # October 2016
        monthly_temp_sum10_16 = sum(avg_temp[638:669])
        avg_temp10_16 = monthly_temp_sum10_16 / 31

        # November 2016
        monthly_temp_sum11_16 = sum(avg_temp[669:699])
        avg_temp11_16 = monthly_temp_sum11_16 / 30

        # December 2016
        monthly_temp_sum12_16 = sum(avg_temp[699:730])
        avg_temp12_16 = monthly_temp_sum12_16 / 31

        # Jan 2017
        monthly_temp_sum1_17 = sum(avg_temp[730:761])
        avg_temp1_17 = monthly_temp_sum1_17 / 31

        # Feb 2017
        monthly_temp_sum2_17 = sum(avg_temp[761:789])
        avg_temp2_17 = monthly_temp_sum2_17 / 28

        # March 2017

        monthly_temp_sum3_17 = sum(avg_temp[789:820])
        avg_temp3_17 = monthly_temp_sum3_17 / 31

        # April 2017
        monthly_temp_sum4_17 = sum(avg_temp[820:850])
        avg_temp4_17 = monthly_temp_sum4_17 / 30

        # May 2017
        monthly_temp_sum5_17 = sum(avg_temp[850:881])
        avg_temp5_17 = monthly_temp_sum5_17 / 31

        # June 2017
        monthly_temp_sum6_17 = sum(avg_temp[881:911])
        avg_temp6_17 = monthly_temp_sum6_17 / 30

        # July 2017
        monthly_temp_sum7_17 = sum(avg_temp[911:942])
        avg_temp7_17 = monthly_temp_sum7_17 / 31

        # August 2017
        monthly_temp_sum8_17 = sum(avg_temp[942:973])
        avg_temp8_17 = monthly_temp_sum8_17 / 31

        # September 2017
        monthly_temp_sum9_17 = sum(avg_temp[973:1003])
        avg_temp9_17 = monthly_temp_sum9_17 / 30

        # October 2017
        monthly_temp_sum10_17 = sum(avg_temp[1003:1034])
        avg_temp10_17 = monthly_temp_sum10_17 / 31

        # November 2017
        monthly_temp_sum11_17 = sum(avg_temp[1034:1064])
        avg_temp11_17 = monthly_temp_sum11_17 / 30

        # December 2017
        monthly_temp_sum12_17 = sum(avg_temp[1064:1095])
        avg_temp12_17 = monthly_temp_sum12_17 / 31



    # Jan 2015
    temp_low += (min(low_days[0:31]))
    temp_high += (max(high_days[0:31]))

    # Feb 2015
    temp_low += (min(low_days[31:59]))
    temp_high += (max(high_days[31:59]))

    # March 2015
    temp_low += (min(low_days[59:90]))
    temp_high += (max(high_days[59:90]))

    # April 2015
    temp_low += (min(low_days[90:120]))
    temp_high += (max(high_days[90:120]))

    # May 2015
    temp_low += (min(low_days[120:151]))
    temp_high += (max(high_days[120:151]))

    # June 2015
    temp_low += (min(low_days[151:180]))
    temp_high += (max(high_days[151:180]))

    # July 2015
    temp_low += (min(low_days[180:211]))
    temp_high += (max(high_days[180:211]))

    # August 2015
    temp_low += (min(low_days[211:242]))
    temp_high += (max(high_days[211:242]))

    # September 2015
    temp_low += (min(low_days[242:272]))
    temp_high += (max(high_days[242:272]))

    # October 2015
    temp_low += (min(low_days[272:303]))
    temp_high += (max(high_days[272:303]))

    # November 2015
    temp_low += (min(low_days[272:303]))
    temp_high += (max(high_days[272:303]))

    # December 2015
    temp_low += (min(low_days[303:333]))
    temp_high += (max(high_days[303:333]))

    # Jan 2016
    temp_low += (min(low_days[333:364]))
    temp_high += (max(high_days[333:364]))

    # Feb 2016
    temp_low += (min(low_days[364:395]))
    temp_high += (max(high_days[364:395]))

    # March 2016
    temp_low += (min(low_days[395:424]))
    temp_high += (max(high_days[395:424]))

    # April 2016
    temp_low += (min(low_days[424:455]))
    temp_high += (max(high_days[424:455]))

    # May 2016
    temp_low += (min(low_days[455:485]))
    temp_high += (max(high_days[455:485]))

    # April 2016
    temp_low += (min(low_days[485:516]))
    temp_high += (max(high_days[485:516]))

    # May 2016
    temp_low += (min(low_days[516:546]))
    temp_high += (max(high_days[516:546]))

    # June 2016
    temp_low += (min(low_days[546:577]))
    temp_high += (max(high_days[546:577]))

    # August 2016

    temp_low += (min(low_days[577:608]))
    temp_high += (max(high_days[577:608]))

    # September 2016

    temp_low += (min(low_days[608:638]))
    temp_high += (max(high_days[608:638]))

    # October 2016

    temp_low += (min(low_days[638:669]))
    temp_high += (max(high_days[638:669]))

    # November 2016

    temp_low += (min(low_days[669:699]))
    temp_high += (max(high_days[669:699]))

    # December 2016

    temp_low += (min(low_days[699:730]))
    temp_high += (max(high_days[699:730]))

    # January 2017

    temp_low += (min(low_days[730:761]))
    temp_high += (max(high_days[730:761]))

    # February 2017

    temp_low += (min(low_days[761:789]))
    temp_high += (max(high_days[761:789]))

    # March 2017

    temp_low += (min(low_days[789:820]))
    temp_high += (max(high_days[789:820]))

    # April 2017

    temp_low += (min(low_days[820:850]))
    temp_high += (max(high_days[820:850]))

    # May 2017

    temp_low += (min(low_days[850:881]))
    temp_high += (max(high_days[850:881]))

    # June 2017
    temp_low += (min(low_days[881:991]))
    temp_high += (max(high_days[881:991]))

    # July 2017
    temp_low += (min(low_days[911:942]))
    temp_high += (max(high_days[911:942]))

    # August 2017
    temp_low += (min(low_days[942:973]))
    temp_high += (max(high_days[942:973]))

    # September 2017
    temp_low += (min(low_days[973:1003]))
    temp_high += (max(high_days[973:1003]))

    # October 2017
    temp_low += (min(low_days[1003:1034]))
    temp_high += (max(high_days[1003:1034]))

    # November 2017
    temp_low += (min(low_days[1034:1064]))
    temp_high += (max(high_days[1034:1064]))

    # December 2017
    temp_low += (min(low_days[1064:1095]))
    temp_high += (max(high_days[1064:1095]))

    final_values += [avg_temp1]
    final_values += [avg_temp2]
    final_values += [avg_temp3]
    final_values += [avg_temp4]
    final_values += [avg_temp5]
    final_values += [avg_temp6]
    final_values += [avg_temp7]
    final_values += [avg_temp8]
    final_values += [avg_temp9]
    final_values += [avg_temp10]
    final_values += [avg_temp11]
    final_values += [avg_temp12]
    final_values += [avg_temp1_16]
    final_values += [avg_temp2_16]
    final_values += [avg_temp3_16]
    final_values += [avg_temp4_16]
    final_values += [avg_temp5_16]
    final_values += [avg_temp6_16]
    final_values += [avg_temp7_16]
    final_values += [avg_temp8_16]
    final_values += [avg_temp9_16]
    final_values += [avg_temp10_16]
    final_values += [avg_temp11_16]
    final_values += [avg_temp12_16]
    final_values += [avg_temp1_17]
    final_values += [avg_temp2_17]
    final_values += [avg_temp3_17]
    final_values += [avg_temp4_17]
    final_values += [avg_temp5_17]
    final_values += [avg_temp6_17]
    final_values += [avg_temp7_17]
    final_values += [avg_temp8_17]
    final_values += [avg_temp9_17]
    final_values += [avg_temp10_17]
    final_values += [avg_temp11_17]
    final_values += [avg_temp12_17]

    month = []

    for i in range(36):
        month += [i + 1]

    plt.xlabel("Month")
    plt.ylabel("Average Temperature per Month")
    plt.title('Average Temperature vs Months')

    for i in range(36):
        plt.errorbar(month[i], final_values[i], yerr=((float(temp_high[i]) - float(temp_low[i]))/ 2.0), color='purple')

    plt.bar(month, final_values)
    plt.show()
