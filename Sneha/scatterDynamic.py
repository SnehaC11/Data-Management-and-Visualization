import matplotlib.pyplot as plt
import numpy as np
x_raw = input("Enter X values: ").split()
y_raw = input("Enter Y values: ").split()
x = np.array(list(map(float, x_raw)))
y = np.array(list(map(float, y_raw)))
plt.scatter(x, y)
plt.title("Dynamic Scatter Plot")
plt.xlabel("X-axis-->")
plt.ylabel("Y-axis-->")
plt.show()