import pandas as pd
import numpy as np

# 1. Raw economic dataset with missing values (NaN) and messy formatting
data = {
    'Country': ['United Kingdom', 'United States', 'Germany', 'Japan', 'Argentina', np.nan],
    'Inflation_Rate_Pct': [3.2, 2.9, 2.5, 0.8, np.nan, 4.1],
    'Unemployment_Rate': [4.0, 3.6, 5.2, 2.5, 7.1, np.nan]
}

df = pd.DataFrame(data)

print("--- Raw Messy Dataset ---")
print(df)

# 2. Drop rows where critical data is completely missing
df_cleaned = df.dropna(subset=['Country', 'Inflation_Rate_Pct'])

print("\n--- Cleaned Dataset (Dropped NaNs) ---")
print(df_cleaned)

# 3. Calculate advanced descriptive statistics
print("\n--- Descriptive Statistics (Summary Report) ---")
print(df_cleaned[['Inflation_Rate_Pct', 'Unemployment_Rate']].describe())
