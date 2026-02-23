import numpy as np
import matplotlib.pyplot as plt
n=int(input("Enter size of array:"))
x=[]
y=[]
for i in range(n):
    x_val=int(input("Enter x value:"))
    x.append(x_val)
    y_val=int(input("Enter y value:"))
    y.append(y_val)
plt.title("Dynamic Line Chart")
plt.xlabel("X-Axis-->")
plt.ylabel("Y-Axis-->")
plt.plot(x, y, marker='o')
plt.show()