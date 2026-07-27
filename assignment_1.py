import pandas as pd

# 1. Load CSV dataset
df = pd.read_csv("Space_Corrected.csv")

# 2. Display first 5 rows
print("--- First 5 Rows ---")
print(df.head())

# 3. Show column names
print("\n--- Column Names ---")
print(df.columns.tolist())

# 4. Display number of rows and columns
print("\n--- Number of Rows and Columns ---")
print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

# 5. Show summary statistics
print("\n--- Summary Statistics ---")
print(df.describe())