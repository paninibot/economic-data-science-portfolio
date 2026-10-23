import pandas as pd

# 1. Create raw economic data dictionary
data = {
    'Country': ['United Kingdom', 'United States', 'Germany', 'Japan', 'Nigeria'],
    'GDP_per_Capita_USD': [46500, 70200, 51200, 39500, 2100],
    'Life_Expectancy_Years': [81.0, 79.0, 81.2, 84.6, 52.7]
}

# 2. Convert dictionary into a Pandas DataFrame (an economic table)
df = pd.DataFrame(data)

print("--- Economic Dataset Preview ---")
print(df)

# 3. Calculate key summary statistics (Mean)
print("\n--- Summary Statistics (Averages) ---")
print(df[['GDP_per_Capita_USD', 'Life_Expectancy_Years']].mean())
