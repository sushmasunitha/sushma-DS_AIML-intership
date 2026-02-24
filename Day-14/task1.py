
import pandas as pd

data = {
    'Transmission': ['Automatic', 'Manual', 'Manual', 'Automatic', 'Manual'],
    'Color': ['Red', 'Blue', 'Green', 'Blue', 'Red']
}

df = pd.DataFrame(data)

print("Original Dataset:\n")
print(df)


df['Transmission'] = df['Transmission'].map({
    'Automatic': 0,
    'Manual': 1
})

print("\nAfter Label Encoding (Transmission):\n")
print(df)


df = pd.get_dummies(df, columns=['Color'], drop_first=True)

print("\nFinal Dataset after One-Hot Encoding (Color):\n")
print(df)