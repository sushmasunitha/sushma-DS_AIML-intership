import pandas as pd

data = {
    "Location": [" New York", "new york", "NEW YORK ", " New york ", "new YORK"]
}

df = pd.DataFrame(data)

print("Original Locations:")
print(df["Location"].unique())

df["Location"] = df["Location"].str.strip()

df["Location"] = df["Location"].str.title()

print("\nCleaned Locations:")
print(df["Location"].unique())