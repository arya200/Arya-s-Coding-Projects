# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “We have not given or received any unauthorized aid on this assignment”
#
# Names:          Arya Ramchandani 627007018
#
# Section:        021
# Assignment:     Lab08b - 1b
# Date:           24 October 2018

def facility(name_list, cost_list, value_list):
    profit = 0

    profit_list = []

    position = 0

    for i in range(len(name_list)):

        profit = float(value_list[i]) - float(cost_list[i])
        profit_list += [profit]
        if profit <= profit_list[i]:
            profit = profit_list[i]
            position = profit_list.index(min(profit_list))

    return (name_list[position], min(profit_list))


number = int(input('Enter the number of industries: '))

name_list = []

cost_list = []

value_list = []

for i in range(number):
    name = input('Enter the name: ')
    name_list += [name]
    cost = input('Enter the annual cost of operation: ')
    cost_list += [cost]
    value = input("Enter the value of the products produced: ")
    value_list += [value]

arr = facility(name_list, cost_list, value_list)
print(arr[0] + str(":"), arr[1])
