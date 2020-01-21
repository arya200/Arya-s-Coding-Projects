print("This program will calculate the production of a well after a given number of days")

print("")

time = float(input("Enter the time(days): "))

prod_rate = float(input("Enter the production rate: "))
decline_rate = float(input("Enter the decline rate: "))
constant = 0.8

fin_prod = prod_rate/((1+((constant*decline_rate*time))**(1/constant)))

print("The final production of the well is:", fin_prod)
