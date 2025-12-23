# shrink_dataset.py

import pandas as pd
import os

# This script takes a very large CSV file and saves a smaller random sample.
# It was used once to create a GitHub-friendly dataset.

INPUT_PATH = "vehicles.csv"          # original large file (not committed)
OUTPUT_PATH = "data/raw_data.csv"    # sampled output
SAMPLE_SIZE = 500

print("Loading large dataset...")
df = pd.read_csv(INPUT_PATH)

print("Original shape:", df.shape)

# Take a random sample
sample_df = df.sample(n=SAMPLE_SIZE, random_state=42)

# Make sure output folder exists
os.makedirs("data", exist_ok=True)

# Save sampled data
sample_df.to_csv(OUTPUT_PATH, index=False)

print("Saved sampled dataset to:", OUTPUT_PATH)
print("Sample shape:", sample_df.shape)
