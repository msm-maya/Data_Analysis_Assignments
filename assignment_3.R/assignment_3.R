# Load dataset
df <- read.csv("Space_Corrected.csv")

# Create dummy score columns
df$Score1 <- (seq_len(nrow(df)) - 1) %% 21 + 70
df$Score2 <- (seq_len(nrow(df)) - 1) %% 16 + 75

# Create Average Score
df$Average_Score <- (df$Score1 + df$Score2) / 2

# Sort data by Average Score (Ascending)
sorted_df <- df[order(df$Average_Score), ]

# Display first 10 rows
print(head(sorted_df[c("Score1", "Score2", "Average_Score")], 10))