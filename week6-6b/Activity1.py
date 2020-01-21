# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Names:          Connor Tisdel 627004745
#                 Chance Smith 727001732
#                 Arya Ramchandani 627007018
#                 Alvin Yolanda Ewaldo 227008703
# Section:        021
# Assignment:     Lab11a - 1
# Date:           5 September 2018

def f(x):

    A = 4
    B = 3
    C = 2
    D = 1

    f_of_x = A * (x ** 3) + B * (x ** 2) + (C * x) + D
    return f_of_x


def deriv(x):

    first  = A*3*(x**2)
    second = B*2*(x)
    third = C

    derivitave = (A*3*(x**2)) + B*2*(x) + C

    return derivitave

def newton_step(x_i):

    a = deriv(x_i)
    b = f(x_i)
    x_i1 = x_i - (b/a)

    return x_i1


def newton(x_i):

    approximations = []

    first = x_i

    approximations += [x_i]

    while True:

        second = newton_step(first)

        approximations += [second]

        if abs(second - first) <= (10 ** -6):

            break

        else:
            first = second

    return approximations

x_i = float(input("Enter the initial guess of x: "))

final = newton(x_i)

print("The final list of approximations is: " , final)




