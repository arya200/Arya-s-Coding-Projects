import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-5, 5, 0.01)
y1 = -25*x*x + x + 20
y2 = 10*x*x + x

fig, ax = plt.subplots()
ax.plot(x, y1, x, y2, color='black')
plt.xlabel('x axis')
plt.ylabel('y axis')
ax.fill_between(x, y1, y2, where=y2 > y1, facecolor='blue', alpha=5.5)
ax.fill_between(x, y1, y2, where=y2 <=y1, facecolor='red', alpha=5.5)
ax.set_title('Fill in Between')

plt.show()