import matplotlib.pyplot as plt
import numpy as np
categories_input = input("Enter categories, separated by commas (e.g., Apples, Bananas): ")
categories = [item.strip() for item in categories_input.split(',')]
sales_input = input("Enter sales data, separated by commas (e.g., 400, 350): ")
sales = [int(item.strip()) for item in sales_input.split(',')]
plt.bar(categories, sales)
plt.xlabel("Fruits")
plt.ylabel("Sales")
plt.title("Dynamic Bar Chart")
plt.show()
