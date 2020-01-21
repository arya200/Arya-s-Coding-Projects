# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “We have not given or received any unauthorized aid on this assignment”
#
# Names:          Arya Ramchandani 627007018
#
# Section:        021
# Assignment:     Lab08b - 3
# Date:           24 October 2018

import csv

month = 0
rate = 0

print("This program meant to create a spreadsheets for the user.")

name = input("Enter a name of the CSV file: ")


with open(name + '.csv', 'w')as f:

    loan = float(input("Enter the amount loaned: "))

    interest_rate = float(input("Enter the annual interest rate(%): "))

    money_per_month = float(input("Enter the amount of money being paid monthly: "))

    monthly_rate = (interest_rate/100)/12

    for month in range(31):

        money = csv.writer(f)
        money.writerow(['Month', 'Total amount of Interest',' Amount remained on the loan'])
        money.writerow([month, rate, loan])

        loan = loan - money_per_month
        amount_added = monthly_rate*loan
        loan = loan + amount_added
        rate = rate + amount_added

        month += 1
        if loan < 0:
            break
        month += 1



