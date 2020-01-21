import numpy as np

print("As a team, we have gone through all required sections of the tutorial, and each team member understands the material.")



A = np.random.random((3,4))
B = np.random.random((4,2))
C = np.random.random((2,3))
D = np.random.random((3,1))

print("This is matrix A " + '\n', A)
print("")
print("This is matrix B "+ '\n', B)
print("")
print("This is matrix C "+ '\n', C)
print("")
print("This is matrix D "+ '\n', D)

E = A@B@C


print("")
print("This is matrix E " + '\n', E)
print("")

print("This is the transposed matrix E" + '\n')
print(E.T)

x = np.linalg.solve(E,D)
print("")
print("This solves the linear system, Ex=D" + '\n', x)


