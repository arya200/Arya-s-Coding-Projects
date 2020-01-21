# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:           Arya Ramchandani
# Section:        021
# Assignment:     lab6b-1
# Date:           10/3/18

#part a

n = float(input("Enter a number in order to perform to the collatz conjecture: "))
check=0

#checking to see if the number if the last nunber is one or not

while(check!=1):
    #checking to see if number is even
    if(n%2==0):
        n=n/2
        print(n)
        check=n

    #else the number will be odd

    else:
        n=(3*n)+1
        print(n)
        check=n







