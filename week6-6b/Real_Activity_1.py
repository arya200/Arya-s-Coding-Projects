# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:           Arya Ramchandani
# Section:        021
# Assignment:     lab6b-1
# Date:           10/3/18

import math
from math import*
print("The cubic equation will be in the formula of Ax^3 + Bx^2 + Cx + D")

#inputting the values
A = float(input("Enter the coefficient for x^3: "))
B = float(input("Enter the coefficient for x^2: "))
C = float(input("Enter the coefficient for x: "))
D = float(input("Enter the last coefficient: "))

#finding the derivitaves with each coefficient separately

first = (3*A)
second = (2*B)
third = C

#joining them all as one string
derivative = str(first) + "x^2" + "+" + str(second) + "x" + "+" + str(C)

print("The derivative is: ", derivative)
x = float(input("Enter an x value: "))
first = first * (x**2)
second = second * (x)

#finding f(x)
f_of_x = A*(x**3) + B*(x**2) + (C * x)+ D

#finding the value of the derrivative
derivative_value = first + second + C
print("The derivative value at x is: " , derivative_value)

#part b

a=0.1
check=1

# 4 steps processes
nx = (A * (x + a) ** 3 + B * (x + a) ** 2 + C * (x + a) + D)

# four steps answers


Equation = (nx - f_of_x) / a


while True:

   a /= 2
   # original function
   f_of_x = (A * x ** 3 + B * x ** 2 + C * x + D)
   # 4 steps processes
   nx = (A * (x + a) ** 3 + B * (x + a) ** 2 + C * (x + a) + D)
   check += 1

   # four steps answers

   Equation2 = (nx - f_of_x) / a

   if abs(Equation2-Equation)<=10**-6:
       break
   else:
       Equation=Equation2



print("It took " + str(check) + " iteration to find the answer.")
print ("The derivative of the function, (f(x+a)-f(x))/a, is: "+str(Equation2))
print ("The difference between the part A and part B is "+str(Equation2-derivative_value))
print ("----------------------------------------------------------------------------------------------------------------------------")

#part c

#log function

x = float(input("Give the value of x for the derivative of log function: "))
a=0.1
check=1
f_of_x = log(x)
# 4 steps processes
nx = log(x+a)

# four steps answers


Equation = (nx - f_of_x) / a


while True:

   a /= 2
   # original function
   f_of_x = log(x)
   # 4 steps processes
   nx = log(x + a)
   check += 1

   # four steps answers

   Equation2 = (nx - f_of_x) / a

   if abs(Equation2-Equation)<=10**-6:
       break
   else:
       Equation=Equation2



print("It took " + str(check) + " iteration to find the answer.")
print ("The derivative of the function, (f(x+a)-f(x))/a, is: "+str(Equation2))
print ("----------------------------------------------------------------------------------------------------------------------------")

#sin x

x = float(input("Give the value of x for the derivative of sin function: "))
a=0.1
check=1
f_of_x = sin(x)
# 4 steps processes
nx = sin(x+a)

# four steps answers


Equation = (nx - f_of_x) / a


while True:

   a /= 2
   # original function
   f_of_x = sin(x)
   # 4 steps processes
   nx = sin(x + a)
   check += 1

   # four steps answers

   Equation2 = (nx - f_of_x) / a

   if abs(Equation2-Equation)<=10**-6:
       break
   else:
       Equation=Equation2



print("It took " + str(check) + " iteration to find the answer.")
print ("The derivative of the function, (f(x+a)-f(x))/a, is: "+str(Equation2))
print ("----------------------------------------------------------------------------------------------------------------------------")

#cos x

x = float(input("Give the value of x for the derivative of cos function: "))
a=0.1
check=1
f_of_x = cos(x)
# 4 steps processes
nx = cos(x+a)

# four steps answers


Equation = (nx - f_of_x) / a


while True:

   a /= 2
   # original function
   f_of_x = cos(x)
   # 4 steps processes
   nx = cos(x + a)
   check += 1

   # four steps answers

   Equation2 = (nx - f_of_x) / a

   if abs(Equation2-Equation)<=10**-6:
       break
   else:
       Equation=Equation2



print("It took " + str(check) + " iteration to find the answer.")
print ("The derivative of the function, (f(x+a)-f(x))/a, is: "+str(Equation2))
print ("----------------------------------------------------------------------------------------------------------------------------")


#tan x

x = float(input("Give the value of x for the derivative of tan function: "))

a=0.1
check=1
f_of_x = tan(x)
# 4 steps processes
nx = tan(x+a)

# four steps answers


Equation = (nx - f_of_x) / a


while True:

   a /= 2
   # original function
   f_of_x = tan(x)
   # 4 steps processes
   nx = tan(x + a)
   check += 1

   # four steps answers

   Equation2 = (nx - f_of_x) / a

   if abs(Equation2-Equation)<=10**-6:
       break
   else:
       Equation=Equation2



print("It took " + str(check) + " iteration to find the answer.")
print ("The derivative of the function, (f(x+a)-f(x))/a, is: "+str(Equation2))
print ("----------------------------------------------------------------------------------------------------------------------------")


















