import matplotlib.pyplot as plt

# Data for the pie chart
slices = [7, 2, 8, 13]
activities = ['Sleeping', 'Eating', 'Working', 'Playing']
cols = ['c', 'm', 'r', 'b']

# Create the pie chart
plt.pie(slices,
        labels=activities,
        colors=cols,
        startangle=90,
        autopct='%1.1f%%')

# Add a title
plt.title('My Daily Activities')

# Display the chart
plt.show()
