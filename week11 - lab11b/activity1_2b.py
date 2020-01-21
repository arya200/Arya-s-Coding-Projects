# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “We have not given or received any unauthorized aid on this assignment”
#
# Names:          Arya Ramchandani 627007018
#
# Section:        021
# Assignment:     Lab08b - 1b
# Date:           24 October 2018

def values(file_name, n):

    data_entry = open(file_name, "r")

    final_sorted_values = []
    array = []
    all_values = []
    real_values = []
    all_real_values = []
    next(data_entry)


    for next_line in data_entry:

        # creates a string of the first line in the file
        s = next_line

        # converts that into a list, without the next line
        s1 = s.split(' ')
        all_values = []
        for i in range(n):

            all_values.append(float(s1[i]))

        all_real_values.append(all_values)





    final_sorted_values = sorted(all_real_values, key=lambda x: x[0])

    print("Ignore the first y value given by the code")

    
    max_value = max(final_sorted_values)
    min_value = min(final_sorted_values)

    x_user_value = float(input("Enter an x value: "))
    b = 0
    x_values = []
    while b < len(final_sorted_values):
        x_values.append(final_sorted_values[b][0])
        b += 1
    counter = 0
    while counter < n:
        y_values = []
        b = 0
        while b < len(final_sorted_values) and counter < len(final_sorted_values):
            y_values.append(final_sorted_values[b][counter])
            b += 1

        if x_user_value <= (x_values[0]):

            # uses the interpolation formula into variable output
            output = ((y_values[1] - y_values[0]) / (x_values[1] - x_values[0])) * (x_user_value - x_values[0]) + \
                     y_values[0]
            print( 'y =', output)

        # checks to see if the x value entered is greater than all the x values inputted
        elif x_user_value >= x_values[len(x_values) - 1]:

            # uses the interpolation formula into variable output
            output = ((y_values[len(y_values) - 1] - y_values[len(y_values) - 2]) / (
                        x_values[len(x_values) - 1] - x_values[len(x_values) - 2])) * \
                     (x_user_value - x_values[len(x_values) - 1]) + y_values[len(y_values) - 1]
            print( 'y =', output)

        # for x values that are part of the inputted values
        else:
            for i in range(len(x_values)):
                if x_user_value == x_values[i]:
                    print( 'y =', y_values[i])
                    break
        counter += 1
        
        
        
    





file_name = input("Enter the name: ")
n = int(input("Enter the dimensions: "))
values(file_name, n)

