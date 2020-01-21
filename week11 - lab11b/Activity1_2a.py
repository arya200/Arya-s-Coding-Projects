# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “We have not given or received any unauthorized aid on this assignment”
#
# Names:          Arya Ramchandani 627007018
#
# Section:        021
# Assignment:     Lab08b - 1b
# Date:           24 October 2018


def f(file_name):

    data_entry = open(file_name, "r")

    # creates two empty strings of x and y values
    x_values = []
    y_values = []
    x_y_values =[]

    # loop which goes through every line
    next(data_entry)
    for next_line in data_entry:
        # creates a string of the first line in the file
        s = next_line

        # converts that into a list, without the next line
        s1 = s.split('\n')
        # extracts the string from the list as an individual string
        s2 = s1[0]
        # splits the string into two individual strings before and after and the comma
        x, y = s2.split(' ')

        # converts the string x and y values into a float and inputs them into the list

        x_values += [float(x)]
        y_values += [float(y)]

    for i in range(len(x_values)):
        list = [x_values[i], y_values[i]]

        x_y_values += [list]

    x_y_sorted = sorted(x_y_values, key=lambda x: x[0])

    x_values =[]
    y_values =[]

    for k in range(len(x_y_sorted)):

        x_values += [x_y_sorted[k][0]]
        y_values += [x_y_sorted[k][1]]

    num_interpolations = int(input("How many interpolations would you like to conduct? "))

    for i in range(num_interpolations):

        x_user_value = float(input("Enter an x value: "))
        # checks to see if the x value entered is lower than all the x values inputted

        if x_user_value <= (x_values[0]):

            # uses the interpolation formula into variable output
            output = ((y_values[1] - y_values[0]) / (x_values[1] - x_values[0])) * (x_user_value - x_values[0]) + \
                     y_values[0]
            print('At x =', x_user_value, 'y =', output)

        # checks to see if the x value entered is greater than all the x values inputted
        elif x_user_value >= x_values[len(x_values) - 1]:

            # uses the interpolation formula into variable output
            output = ((y_values[len(y_values) - 1] - y_values[len(y_values) - 2]) / (
                        x_values[len(x_values) - 1] - x_values[len(x_values) - 2])) * \
                     (x_user_value - x_values[len(x_values) - 1]) + y_values[len(y_values) - 1]
            print('At x =', x_user_value, 'y =', output)

        # for x values that are part of the inputted values
        else:
            for i in range(len(x_values)):
                if x_user_value == x_values[i]:
                    print('At x =', x_user_value, 'y =', y_values[i])
                    break



    data_entry.close()

file_name = input("Enter the name of the file: ")

f(file_name)
