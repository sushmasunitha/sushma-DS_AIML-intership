
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

data = {
    "SquareFootage": [800, 1000, 1200, 1500, 1800, 2000, 2200, 2500, 2800, 3000],
    "Price": [150000, 200000, 220000, 300000, 350000, 400000, 420000, 500000, 550000, 600000],
    "Bedrooms": [2, 2, 3, 3, 3, 4, 4, 4, 5, 5],
    "Bathrooms": [1, 2, 2, 2, 3, 3, 3, 4, 4, 4]
}

df = pd.DataFrame(data)

corr_matrix = df.corr()
print("Correlation Matrix:\n")
print(corr_matrix)


plt.figure()
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()


print("\nHighly Correlated Feature Pairs (Correlation > 0.8):\n")

for i in range(len(corr_matrix.columns)):
    for j in range(i):
        if abs(corr_matrix.iloc[i, j]) > 0.8:
            print(f"{corr_matrix.columns[i]} and {corr_matrix.columns[j]} -> {corr_matrix.iloc[i, j]}")

plt.figure()
sns.boxplot(y=df["Price"])
plt.title("Boxplot of Price")
plt.ylabel("Price")
plt.show()