from math import *
import math
print("This program will calculate the sheer stress")

print("")

normal_stress = float(input("Enter the value for nomral stress: "))
cohesion = float(input("Enter the value for cohesion: "))
angle_friction = float(input("Enter the value for angle of friction(degrees): "))

sheer_stress = float(cohesion+(normal_stress*tan(math.radians(angle_friction))))

print("The sheer stress is:", sheer_stress)