import pandas as pd

# Load dataset
df = pd.read_csv("Space_Corrected.csv")

# 1. Create dummy score columns
df["Score1"] = (df.index % 21) + 70      # 70–90
df["Score2"] = (df.index % 16) + 75      # 75–90

# 2. Create 'Average Score' column
df["Average Score"] = df[["Score1", "Score2"]].mean(axis=1)

# 3. Apply condition
df["Status"] = df["Average Score"].apply(
    lambda x: "Pass" if x >= 85 else "Fail"
)

# Display output
print(df[["Score1", "Score2", "Average Score", "Status"]].head())