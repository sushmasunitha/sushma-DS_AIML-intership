import numpy as np
import pandas as pd

np.random.seed(42)
data = np.random.normal(loc=50, scale=10, size=1000)

data = np.append(data, [120, 130, -20])

df = pd.DataFrame(data, columns=["Value"])

mu = df["Value"].mean()
sigma = df["Value"].std()

print("Mean (μ):", round(mu, 2))
print("Standard Deviation (σ):", round(sigma, 2))

df["z_score"] = (df["Value"] - mu) / sigma

outliers = df[np.abs(df["z_score"]) > 3]

print("\nOutliers where |Z| > 3:")
print(outliers)

print("\nTotal Outliers Found:", len(outliers))