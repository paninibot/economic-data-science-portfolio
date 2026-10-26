import pandas as pd
import numpy as np

# 1. Panel dataset of global economic indicators
data = {
    'Country': ['United Kingdom', 'United States', 'Germany', 'Japan', 'Argentina', 'Brazil', 'South Korea'],
    'GDP_Growth_Pct': [1.2, 2.5, -0.3, 1.0, -1.5, 2.9, 1.4],
    'Inflation_Rate_Pct': [3.2, 2.9, 2.5, 0.8, 140.0, 4.1, 2.1],
    'Unemployment_Rate': [4.0, 3.6, 5.2, 2.5, 7.1, 7.8, 2.8]
}

df = pd.DataFrame(data)

print("--- Full Global Macroeconomic Panel ---")
print(df)

# 2. Single-Condition Vectorized Filter: High-growth economies (> 1.5%)
high_growth = df[df['GDP_Growth_Pct'] > 1.5]
print("\n--- High Growth Economies (GDP Growth > 1.5%) ---")
print(high_growth[['Country', 'GDP_Growth_Pct']])

# 3. Multi-Condition Vectorized Filter: Stable growth with low inflation
# Growth > 0% AND Inflation < 3.0%
stable_economies = df[(df['GDP_Growth_Pct'] > 0.0) &
                      (df['Inflation_Rate_Pct'] < 3.0)]
print("\n--- Stable Economies (Growth > 0% & Inflation < 3.0%) ---")
print(stable_economies[['Country', 'GDP_Growth_Pct', 'Inflation_Rate_Pct']])

# 4. Conditional Vectorized Assignment using np.where
# Classify economies into 'Recession' or 'Expansion'
df['Economic_Status'] = np.where(
    df['GDP_Growth_Pct'] < 0, 'Recession', 'Expansion')

print("\n--- Final Dataset with Classified Economic Status ---")
print(df[['Country', 'GDP_Growth_Pct', 'Economic_Status']])
