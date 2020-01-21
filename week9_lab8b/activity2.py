# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “We have not given or received any unauthorized aid on this assignment”
#
# Names:          Arya Ramchandani 627007018
#
# Section:        021
# Assignment:     Lab08b - 2
# Date:           24 October 2018

# stores the total limit of values the user wants to enter
limit = int(input("How many values of temperature do you have? "))

file1 = open("Celsius.dat","w")
file2 = open("Fahrenheit.dat","w")

for i in range(limit):
    celsius = float(input("Enter the temperature value in celsius: "))
    file1.write(str(celsius) + '\n')

    # converts the celsius value into fahrenheit and writes them into a file
    fahrenheit = (celsius * (9/5)) + 32
    file2.write(str(fahrenheit) + '\n')

file1.close()
file2.close()


