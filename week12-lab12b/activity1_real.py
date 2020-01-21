# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:           Arya Ramchandani 627007018
# Section:        021
# Assignment:     Lab 12b
# Date:           11th November, 2018

import turtle as t

num = int(input("Enter the number(1-100): "))


def top_left():
    '''Moves turtle to top left corner of screen'''

    t.penup()
    t.left(90)
    t.forward(400)
    t.left(90)
    t.forward(600)
    t.right(180)
    t.pendown()


def single():
    '''Draws a single tally line'''

    t.right(90)
    t.forward(50)


def next_pos():
    '''Move turtle for next tally position'''

    t.left(90)
    t.penup()
    t.forward(10)
    t.left(90)
    t.forward(50)
    t.right(90)
    t.pendown()


def fifth_pos():
    '''Moves turtle in position for diagnol tally'''

    t.left(180)


def diagnol():
    '''Draws diagnol tally'''

    t.right(135)
    t.forward(70)
    t.penup()
    t.backward(70)
    t.right(180)
    t.right(45)
    t.penup()
    t.forward(25)
    t.right(180)
    t.pendown()


def row():
    '''Moves turtle to start a new row'''

    t.penup()
    t.right(90)
    t.forward(130)
    t.right(90)
    t.forward(250)
    t.left(180)
    t.pendown()


top_left()
t.speed(10)

for i in range(1, num + 1):
    if (i % 5 == 0):

        diagnol()
        fifth_pos()

    else:

        single()
        next_pos()

    if (i % 25 == 0):

        row()

print(help(top_left))
print(help(single))
print(help(next_pos))
print(help(fifth_pos))
print(help(diagnol))
print(help(row))
input()

