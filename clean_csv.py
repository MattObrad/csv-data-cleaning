# clean_csv.py

import pandas as pd

# Simple script to clean a messy CSV file
# Just practicing basic pandas data cleaning

print("Reading raw data...")
df = pd.read_csv("data/raw_data.csv")

print("Starting shape:", df.shape)

# Clean up column names so they’re easier to work with
df.columns = (
    df.columns
    .str.lower()
    .str.strip()
    .str.replace(" ", "_")
)

# Remove duplicate rows
rows_before = len(df)
df = df.drop_duplicates()
rows_after = len(df)

print(f"Removed {rows_before - rows_after} duplicate rows")

# Fill missing text values
text_columns = df.select_dtypes(include="object").columns
df[text_columns] = df[text_columns].fillna("unknown")

# Clean numeric columns that are stored as text
for col in ["price", "odometer"]:
    if col in df.columns:
        df[col] = (
            df[col]
            .astype(str)
            .str.replace("$", "", regex=False)
            .str.replace(",", "", regex=False)
            .str.strip()
        )
        df[col] = pd.to_numeric(df[col], errors="coerce")

# Drop rows that don’t have a price
if "price" in df.columns:
    before_price = len(df)
    df = df[df["price"].notna()]
    after_price = len(df)

    print(f"Removed {before_price - after_price} rows with no price")

# Save the cleaned data
df.to_csv("data/cleaned_data.csv", index=False)

print("Saved cleaned file to data/cleaned_data.csv")
print("Final shape:", df.shape)
