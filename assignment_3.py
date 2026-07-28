import pandas as pd

# Load dataset
df = pd.read_csv("Space_Corrected.csv")

# Create dummy score columns
df["Score1"] = (df.index % 21) + 70
df["Score2"] = (df.index % 16) + 75

# Create Average Score
df["Average Score"] = df[["Score1", "Score2"]].mean(axis=1)

# Sort data by Average Score (Ascending)
sorted_df = df.sort_values(by="Average Score", ascending=True)

# Display first 10 rows
print(sorted_df[["Score1", "Score2", "Average Score"]].head(10))