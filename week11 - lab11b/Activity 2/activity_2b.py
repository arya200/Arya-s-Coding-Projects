# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “We have not given or received any unauthorized aid on this assignment”
#
# Names:          Arya Ramchandani 627007018
#
# Section:        021
# Assignment:     Lab08b - 1b
# Date:           24 October 2018

def mailing_label(name, city, state, zip_code, address, address1):

    print(name)
    print(address)
    if (address1 != ''):
        print(address1)
    print(city, state)
    print(zip_code)


name = input("Enter your name: ")
city = input("Enter your city: ")
state = input("Enter your state: ")
zip_code = input("Enter your zip code: ")
address = input("Enter the first line of address: ")
address1 = input("Enter your second line of address(Press enter if none): ")
mailing_label(name, city, state, zip_code, address, address1)

