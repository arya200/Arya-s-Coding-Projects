# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “We have not given or received any unauthorized aid on this assignment”
#
# Names:          Arya Ramchandani 627007018
#
# Section:        021
# Assignment:     Lab07b - 3
# Date:           10 October 2018

# creating empty dictionary
storage = {}

# asking how many usernames and passsword exist
total_values = int(input("How many values do you want to store: "))

# inputting the usernames and passwords
for i in range(total_values):
    username = str(input("What is the username: "))
    password = str(input("What is the password: "))
    storage[username] = password

print("")

# running the loop to see if they enter the right username and password

while True:
    test_username = str(input("Enter your username: "))

    # if username exists in dictionary

    if(test_username in storage):
        test_password = str(input("Enter your password: "))

        # if username matches password.

        if storage[test_username] == test_password:
            print("You can pass")
            break

        # if wrong password entered can try again

        else:
            print("Wrong password, try again below")
            continue

    # if wrong username entered can try again

    else:
        print("Wrong username, try again")
        continue



