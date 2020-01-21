# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “We have not given or received any unauthorized aid on this assignment”
#
# Names:          Connor Tisdel 627004745
#                 Chance Smith 727001732
#                 Arya Ramchandani 627007018
#                 Alvin Yolanda Ewaldo 227008703
# Section:        021
# Assignment:     Lab07a - 1
# Date:           8 October 2018

#this variable exists in order to keep the loop running until a negative number is entered.
number_of_days = int(input("Enter the total number of days: "))

#this is an empty list
Widget = []

#input loop
while number_of_days >= 0:
    prod = float(input("Enter the number of widgets produced for each day, and enter a negative number when you want to stop: "))

    #if a negative value is entered the loop will break

    if prod < 0:
        break
    else:
        # this is adding a new value to the array continuously
        Widget += [prod]

print("The maximum number of intervals is:", str(len(Widget)-1))

#the day interval value
interval = 0

#the check until which the loop will run
check = len(Widget)-1


while interval<(len(Widget)-1):

    #incrementing the day intervals
    interval+=1

    # calculates the number of increasing components
    inc_num = 0

    # calculates the number of increasing components
    dec_num = 0


    for i in range(check):

        #checking to see if the value is increasing or decreasing
        if(Widget[i] < Widget[i+interval]):
            inc_num+=1

        elif(Widget[i] > Widget[i+interval] ):
            dec_num+=1
    #decreases the range value each time it exits the four loop
    check-=1

    #calculating the increasing percent
    increasing_percent = float((inc_num/(len(Widget) - interval))*100)

    #Rounding the percent to one decimal place
    inc_percent = round(increasing_percent,1)

    #Calculating the decreasing percent
    decreasing_percent = float((dec_num/(len(Widget) - interval))*100)

    #Rounding the percent to one decimal place
    dec_percent = round(decreasing_percent,1)

    print("For", interval, "-day intervals", inc_percent, "were increasing and ", dec_percent, "were decreasing")






