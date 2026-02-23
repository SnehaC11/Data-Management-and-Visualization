import numpy as np
import matplotlib.pyplot as plt
user_input = input("Enter data values separated by spaces: ")
data_list = [int(x) for x in user_input.split()]
data = np.array(data_list)
plt.hist(data, bins=5, color='purple', edgecolor='black')
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.title("Dynamic Histogram")
plt.show()