import matplotlib.pyplot as plt
x = list(map(int, input("Enter x axis data:").split()))
y = list(map(int, input("Enter y axis data:").split()))

if len(x) != len(y):
    print("X AND Y MUST HAVE SAME NUMBER OF VALUES")
else:
    plt.plot(x, y)

    plt.xlabel("X Axis")
    plt.ylabel("y Axis")
    plt.title("Static Line Chart")

    plt.show()
