import matplotlib.pyplot as plt

activities1 = input("Enter 4 activities separated by a spaces: ")
activities = activities1.split()
slices1 = input("Enter the values separated by a space: ")
slices2 = slices1.split()
slices = [int(s) for s in slices2]
cols = ['c', 'm', 'r', 'b']

plt.pie(slices,
        labels=activities,
        colors=cols,
        startangle=90,
        autopct='%1.1f%%')

plt.title('My Daily Activities')
plt.show()