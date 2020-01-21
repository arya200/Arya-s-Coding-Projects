import math

from math import *
print("This program will calculate the angle between two points, as seen by an observer")

print("")

print("Enter the 3D position of the observer below")

x_obs = float(input("Enter the x value: "))
y_obs = float(input("Enter the y value: "))
z_obs = float(input("Enter the z value: "))

print("")

print("Enter the 3D position of the first observed point below")

x1 = float(input("Enter the x1 value: "))
y1 = float(input("Enter the y1 value: "))
z1 = float(input("Enter the z1 value: "))

print("")

print("Enter the 3D position of the second observed point below")

x2 = float(input("Enter the x2 value: "))
y2 = float(input("Enter the y2 value: "))
z2 = float(input("Enter the z2 value: "))

print("")

# The vector from the first point to the observer will have the variables below

v1 = float(x1-x_obs)
v2 = float(y1-y_obs)
v3 = float(z1-z_obs)

# The vector from the second point to the observer will have the variables below

v_1 = float(x2-x_obs)
v_2 = float(y2-y_obs)
v_3 = float(z2-z_obs)

magnitude1 = float(sqrt((v1**2)+(v2**2)+(v3**2)))
magnitude2 = float(sqrt(v_1**2)+(v_2**2)+(v_3**2))

# The normalised vector from the first point to the observer will have the variables below

u1 = v1/magnitude1
u2 = v2/magnitude1
u3 = v3/magnitude1

# The normalised vector from the second point to the observer will have the variables below

u_1 = v_1/magnitude2
u_2 = v_2/magnitude2
u_3 = v_3/magnitude2

dot_product = float((u1*u_1) + (u2*u_2) + (u3*u_3))

angle = acos((dot_product))

print("The angle(degrees) between the two points is:", degrees(angle))


