# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:           Arya Ramchandani
# Section:        021
# Assignment:     lab1-5
# Date:           2/9/18



import math
from math import *
print("Arya Ramchandani, 627007018, 021")
print("I have been playing the drums for 6 years")

print("")

Current = 5
Resistance = 20
print(Current*Resistance)

print("")

mass = 100
velocity = 21
print(0.5*(mass*(velocity**2)))

print("")

viscosity = 1.2
velocity = 100
dimension = 2.5
print((velocity*dimension)/viscosity)

print("")

temp = 2200
boltzman = (10**-8)
print(((5.67)*boltzman)*(temp**4))

print("")

time=20
prod_rate=100
decline_rate=2
constant=0.8

print(prod_rate/((1+((constant*decline_rate*time))**(1/constant))))

print("")

arrival_rate=20
service_rate=35
print(((arrival_rate/service_rate)**2)/(1-(arrival_rate/service_rate)))

print("")

normal_stress=20
cohesion=2
angle_friction=35
print(cohesion+(normal_stress*tan(math.radians(angle_friction))))

print("")

wavelength=7.5*(10**-7)
distance=1*(10**-6)
print(asin(wavelength)/(2*distance))