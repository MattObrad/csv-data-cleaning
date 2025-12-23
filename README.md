# CSV Data Cleaning Script

This is a small Python project I built to practice cleaning messy CSV files using pandas. The goal was to simulate a very common real-world task: taking a raw dataset, fixing common issues, and saving a cleaned version that’s easier to work with for analysis or visualization.

Dataset can be found here: https://www.kaggle.com/datasets/austinreese/craigslist-carstrucks-data?resource=download 

## What this project does
- Reads a raw CSV file
- Standardizes column names
- Removes duplicate rows
- Handles missing text values
- Cleans numeric columns that are stored as text
- Writes out a cleaned CSV file

## Dataset
The original dataset is very large (over 1GB), so this repository includes a small random sample of the data used for demonstration and reproducibility. The full dataset is not included.

## How to run
Install dependencies:
pip install pandas

Run the script from the project directory:
python clean_csv.py

The cleaned output will be saved to:
data/cleaned_data.csv

## Notes
This script is designed for small datasets and basic preprocessing. For larger files or production use, additional steps like chunked reads or database-based workflows would be more appropriate.
