import numpy as np
import matplotlib.pyplot as plt
data=np.array([10,20,30,35,43,45])
plt.hist(data,bins=5,color='purple',edgecolor='black')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title("Static Histogram")
plt.show()