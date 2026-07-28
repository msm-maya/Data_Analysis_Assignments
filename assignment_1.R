# 1. Load CSV Dataset
df <- read.csv("Space_Corrected.csv")

# 2. First 5 rows
head(df, 5)

# 3. Column names
colnames(df)

# 4. Total rows and columns
dim(df)

# 5. Summary statistics
summary(df)