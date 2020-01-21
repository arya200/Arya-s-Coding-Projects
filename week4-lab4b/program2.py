# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:           Arya Ramchandani
# Section:        021
# Assignment:     lab4b-2
# Date:           23/9/18

print("This program is to determine the whether a person is underweight, healthy weight, obese, or overweight")

print("Please enter your weight in kilograms: ")

weight = float(input())

print("Please enter your height in meters: ")

height = float(input())

BMI = weight/(height**2)

if(BMI < 18.5):
    print("You are underweight")

elif(18.5 <= BMI <= 24.9 ):
    print("You are at a healthy weight")

elif(25.0 <= BMI <= 29.9):
    print("You are overweight")

elif(BMI >= 30.0):
    print("You are obese")






