
# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:           Arya Ramchandani
# Section:        021
# Assignment:     lab2b-2
# Date:           12/9/18

t1=13
pos1_x=1
pos1_y=3

pos1_z=7
t2=84
pos2_x=23
pos2_y=-5
pos2_z=10
t3=50

vel_x=((pos2_x-pos1_x)/(t2-t1))
vel_y=((pos2_y-pos1_y)/(t2-t1))
vel_z=((pos2_z-pos1_z)/(t2-t1))

fin_pos_x =(vel_x*(t3-t1)+pos1_x)
print(fin_pos_x)
fin_pos_y =(vel_y*(t3-t1)+pos1_y)
print(fin_pos_y)
fin_pos_z =(vel_z*(t3-t1)+pos1_z)
print(fin_pos_z)

