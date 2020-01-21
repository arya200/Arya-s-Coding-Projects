from math import *

print("This program is to calculate the kinetic energy of an object ")

mass = (float(input("Please enter the mass(Kg) of the object: ")))

velocity = (float(input("Please enter the velocity(m/s) of the object: ")))

print("")

ke = float(0.5*(mass)*(velocity**2))

print("The kinetic energy(joules) is:", ke)
