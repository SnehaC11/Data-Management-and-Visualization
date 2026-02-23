import matplotlib.pyplot as plt
data = [12,20,11,7,4,24,33,17,1,3]

plt.hist(data, bins=5)

plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Histogram")

plt.show()