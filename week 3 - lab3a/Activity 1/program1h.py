from math import *

val1 = float(input("Please enter the first Richter scale value: "))
val2 = float(input("Please enter the second Richter scale value: "))
rat = float(10**(1.5*(val1-val2)))
print("Measuring the change in energy", val1, "earthquake is", rat, "times the energy of", val2, "earthquake.")