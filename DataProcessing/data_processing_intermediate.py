# data_processing_intermediate.py
import pandas as pd

# Read CSV
data = pd.read_csv("data.csv")  # CSV with at least 'Name' and 'Score'

# Clean data
data = data.drop_duplicates()
data = data.dropna()  # Remove rows with missing values

# Group by Name and calculate stats
grouped = data.groupby('Name')['Score'].agg(['mean', 'max', 'min', 'count'])
print("Grouped Statistics:")
print(grouped)

# Save cleaned data and grouped stats
data.to_csv("data_cleaned.csv", index=False)
grouped.to_csv("data_stats.csv")
print("\nCleaned data saved as 'data_cleaned.csv' and stats as 'data_stats.csv'")
