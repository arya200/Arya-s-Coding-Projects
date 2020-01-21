
import matplotlib.pyplot as plt
import numpy as np

y = np.random.normal(loc=0.1, scale=2, size=10000)
y = y[(y > 0) & (y < 1)]
y.sort()
x = np.arange(len(y))

plt.subplot(111)
plt.plot(x, y)
plt.yscale('log')
plt.title('log')
plt.grid(True)

plt.show()