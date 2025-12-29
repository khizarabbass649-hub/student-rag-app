import pandas as pd

# Load raw data
df = pd.read_csv("students_raw.csv")

# Remove duplicates
df = df.drop_duplicates()

# Fill missing age with average
df["Age"] = df["Age"].fillna(df["Age"].mean())

# Fill missing city
df["City"] = df["City"].fillna("Unknown")

# Fix invalid emails
df["Email"] = df["Email"].apply(
    lambda x: x if "@" in x and "." in x else "invalid@email.com"
)

# Save cleaned data
df.to_csv("students_cleaned.csv", index=False)

print("Data cleaned successfully!")
