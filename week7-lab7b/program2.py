# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “We have not given or received any unauthorized aid on this assignment”
#
# Names:          Arya Ramchandani 627007018
#
# Section:        021
# Assignment:     Lab07b - 2
# Date:           10 October 2018

from math import*
vectorA = []
vectorB = []

dimension_a = int(input("Enter the dimension of the first vector(A): "))
dimension_b = int(input("Enter the dimension of the second vector(B): "))

for i in range(dimension_a):
    point = float(input("Enter the points, in order: "))
    vectorA += [point]


for i in range(dimension_b):
    point = float(input("Enter the points, in order: "))
    vectorB += [point]


print("Vector A : ", vectorA)
print("Vector B : ", vectorB)

# the magnitude of A and B
magnitude_A=0
magnitude_B=0

for i in range(dimension_a):
    magnitude_A += ((vectorA[i])**2)


for k in range (dimension_b):
    magnitude_B += ((vectorB[k])**2)

final_magnitudeA = sqrt(magnitude_A)
final_magnitudeB = sqrt(magnitude_B)

print("The magnitude of vector A is:", final_magnitudeA)
print("The magnitude of vector B is: ", final_magnitudeB)

# A+B

sum1=[]
for j in range(dimension_a):
    sum1 += [vectorA[j]+vectorB[j]]

print("The sum of vector A and vector B is: ", sum1)

# A-B

sum2 = []
for k in range(dimension_b):

    sum2 += [vectorA[k]-vectorB[k]]

print("The difference of vector A and vector B is: ", sum2)

# A.B
final_dot_product = 0
for i in range(dimension_a):

    dot_product = vectorA[i] * vectorB[i]
    final_dot_product += dot_product

print("The dot product of vector A and vector B is: ", final_dot_product)






