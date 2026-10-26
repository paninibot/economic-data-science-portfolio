import pandas as pd

# 1. Global economic panel dataset with regional classifications
data = {
    'Country': ['United Kingdom', 'United States', 'Germany', 'Japan', 'Argentina', 'Brazil', 'South Korea', 'Nigeria', 'Egypt'],
    'Region': ['Europe', 'North America', 'Europe', 'Asia', 'South America', 'South America', 'Asia', 'Africa', 'Africa'],
    'Nominal_GDP_Billions': [3330, 27360, 4450, 4210, 630, 2130, 1710, 375, 470],
    'Inflation_Rate_Pct': [3.2, 2.9, 2.5, 0.8, 140.0, 4.1, 2.1, 24.5, 33.0]
}

df = pd.DataFrame(data)

print("--- Original Global Panel Dataset ---")
print(df)

# 2. Single-Metric Aggregation: Average Inflation Rate by Region
regional_inflation = df.groupby(
    'Region')['Inflation_Rate_Pct'].mean().reset_index()

print("\n--- Average Inflation Rate by Region ---")
print(regional_inflation)

# 3. Multi-Metric Aggregation using .agg()
regional_summary = df.groupby('Region').agg(
    Total_GDP=('Nominal_GDP_Billions', 'sum'),
    Average_Inflation=('Inflation_Rate_Pct', 'mean'),
    Country_Count=('Country', 'count')
).reset_index()

print("\n--- Comprehensive Regional Economic Summary ---")
print(regional_summary)
