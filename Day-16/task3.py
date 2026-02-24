import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)

population = np.random.exponential(scale=50000, size=10000)

plt.figure()
sns.histplot(population, kde=True)
plt.title("Original Population (Right-Skewed)")
plt.show()

sample_means = []

for _ in range(1000):
    sample = np.random.choice(population, size=30)
    sample_means.append(np.mean(sample))

df_means = pd.DataFrame(sample_means, columns=["Sample Mean"])

plt.figure()
sns.histplot(df_means["Sample Mean"], kde=True)
plt.title("Distribution of Sample Means (n=30)")
plt.show()

print("Original Population Mean:", round(np.mean(population), 2))
print("Mean of Sample Means:", round(df_means["Sample Mean"].mean(), 2))