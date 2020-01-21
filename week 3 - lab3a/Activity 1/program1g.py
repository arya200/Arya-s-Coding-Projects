from math import *

vol = float(input("Please enter the voltage: "))
print("The voltage level (power gain) measured in Decibel Volts(dBV) is:", str(20*log10(vol)))