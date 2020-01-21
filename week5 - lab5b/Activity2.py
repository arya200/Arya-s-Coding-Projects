

strain = float(input("Enter the strain value:"))

# this is the line from O to A

if( 0 <= strain <= 0.01):
    stress = (1/4100) * strain
    print("The value of the stress is:", stress, "It is in the increasing linear elastic region")

# this is the line from A to C

elif( 0.01 < strain <=0.06 ):
    stress = (20 * strain) + 40.8
    print("The value of the  stress is:", stress, "It is in the plastic region")

# this is the line from C to D

elif( 0.06 < strain <= 0.17):
    stress = ((1800/11) * strain) + (354/11)
    print("The value of the  stress is:", stress, "It is in the strain hardening region")

# this is the line from D to E

elif( 0.17 < strain <= 0.26):
    stress = ((-1000/9) * strain) + (710/9)
    print("The value of the  stress is:", stress, "It is in the necking region")

