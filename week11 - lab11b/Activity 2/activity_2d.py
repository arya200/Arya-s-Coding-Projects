# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “We have not given or received any unauthorized aid on this assignment”
#
# Names:          Arya Ramchandani 627007018
#
# Section:        021
# Assignment:     Lab08b - 1b
# Date:           24 October 2018


def name(file_name):
    
    import csv


    with open(file_name + ".csv", 'w')as f:
        tsv = open(file_name[:-4]+'.tsv', 'w')
        line = f.readline()
        while f != '':
            value = line.split(',')
            tsv_line = ''
            for i in range(len(value)):
                tsv_line += value[i]
                if i != len(value)-1:
                    tsv_line += '\t'
            tsv.write(tsv_line)
            line = f.readline()

        tsv.close()

