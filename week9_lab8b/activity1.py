# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “We have not given or received any unauthorized aid on this assignment”
#
# Names:          Arya Ramchandani 627007018
#
# Section:        021
# Assignment:     Lab08b - 1
# Date:           24 October 2018


file = input("Enter the name you would like to assign to the file: ")

data_entry = open(file, 'w')

independent_variable_name = input("What is your independent variable: ")

dependant_variable_name = input("What is your dependant variable: ")

# asks the user how many total values it has

limit = int(input("How many data values do you have: "))


print("Please enter the x values in order of lowest to highest")

data_entry.write(independent_variable_name + ',' + dependant_variable_name + '\n')

for i in range(limit):

        # inputting the x values
        independent_variable = (input("What is the value of " + independent_variable_name + ": "))

        # inputting the y values
        dependant_variable =(input("What is the value of " + dependant_variable_name + ": "))

        # creates one big string to enter into the loop

        write_example = str(independent_variable) + " " + str(dependant_variable) + '\n'

        data_entry.write(write_example)

data_entry.close()






