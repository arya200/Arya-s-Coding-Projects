# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Names:          Connor Tisdel 627004745
#                 Chance Smith 727001732
#                 Arya Ramchandani 627007018
#                 Alvin Yolanda Ewaldo 227008703
# Section:        021
# Assignment:     Lab02 - 3
# Date:           3 September 2018

Pos_one = 50
Pos_two = 615
Time_one = 30
Time_two = 45
Measure_time = 37

print("The distance (meters) traveled at 37 seconds is: ")
print(Pos_one + (Measure_time - Time_one) * ((Pos_two - Pos_one) / (Time_two - Time_one)))
