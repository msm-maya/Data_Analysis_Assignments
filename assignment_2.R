# Load dataset
df <- read.csv("Space_Corrected.csv")

# 1. Create dummy score columns
df$Score1 <- (seq_len(nrow(df)) - 1) %% 21 + 70
df$Score2 <- (seq_len(nrow(df)) - 1) %% 16 + 75

# 2. Create 'Average Score' column
df$Average_Score <- (df$Score1 + df$Score2) / 2

# 3. Apply condition
df$Status <- ifelse(df$Average_Score >= 85, "Pass", "Fail")

# Display output
print(head(df[c("Score1", "Score2", "Average_Score", "Status")]))
