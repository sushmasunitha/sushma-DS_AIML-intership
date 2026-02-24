
import matplotlib.pyplot as plt

plt.subplot(1, 2, 1)

categories = ['Electronics', 'Clothing', 'Home']
sales = [300, 450, 200]

plt.bar(categories, sales)
plt.title("Sales by Category")
plt.xlabel("Product Categories")
plt.ylabel("Sales")

plt.subplot(1, 2, 2)

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
trend_sales = [100, 150, 130, 170, 200]

plt.plot(months, trend_sales)
plt.title("Monthly Sales Trend")
plt.xlabel("Months")
plt.ylabel("Sales")

plt.tight_layout()

plt.show()