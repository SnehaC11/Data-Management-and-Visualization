import matplotlib.pyplot as plt
import numpy as np
x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([55, 60, 62, 68, 70, 75])
plt.scatter(x, y)
plt.title("Static Scatter Plot")
plt.xlabel("X-axis-->")
plt.ylabel("Y-axis-->")
plt.show()