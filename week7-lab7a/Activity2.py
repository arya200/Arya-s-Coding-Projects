# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “We have not given or received any unauthorized aid on this assignment”
#
# Names:          Connor Tisdel 627004745
#                 Chance Smith 727001732
#                 Arya Ramchandani 627007018
#                 Alvin Yolanda Ewaldo 227008703
# Section:        021
# Assignment:     Lab07a - 2
# Date:           9 October 2018

from math import*

Player_Name = []
total_score = []
first_round = 0
second_round = 0
name = " "

# has the player enter their first and second round scores and name, also creates one list of scores
while first_round >= 0:
   first_round = float(input("Enter your first round score:"))
   if first_round > 0:
       second_round = float(input("Enter your second round score:"))
       total_score += [first_round + second_round]
       name = str(input("Enter your name: "))
       Player_Name += [name]


# sorts out the total scores in a ascending
for i in range(len(total_score)):
    for j in range (len(total_score)):
        if(total_score[i]<total_score[j]):

            intermediate = total_score[j]
            name_intermediate = Player_Name[j]
            total_score[j] = total_score[i]
            Player_Name[j] = Player_Name[i]
            total_score[i] = intermediate
            Player_Name[i] = name_intermediate

# finds the median if the input number is even
if(len(total_score)%2==0):
    term_number = int((len(total_score)+1)/2)
    first_term = total_score[term_number]
    second_term = total_score[term_number-1]
    median = (first_term+second_term)/2

# finds out the median when input is odd
else:
    term_number = int(len(total_score) / 2)
    median = total_score[term_number]

final_names = []

# takes the players names and divides it up into whether or not they made the cut or not
for k in range(len(Player_Name)):
    if(total_score[k]<=median):
        final_names += [Player_Name[k]]

# prints out the names of the players of those who made the cut and who didn't
check = len(final_names)
print("These players did not make the cut: ", Player_Name[check:])
print("These players did make the cut: ", final_names)


