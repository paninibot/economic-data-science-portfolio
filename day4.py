import pandas as pd

# 1. Create a global economic dataset
data = {
    'Country': ['United Kingdom', 'United States', 'Germany', 'Japan', 'Argentina', 'Nigeria', 'India'],
    'GDP_per_Capita_USD': [46500, 70200, 51200, 39500, 10500, 2100, 2300],
    'Inflation_Rate_Pct': [3.2, 2.9, 2.5, 0.8, 45.0, 4.1, 6.5]
}

df = pd.DataFrame(data)

print("--- Original Global Dataset ---")
print(df)

# 2. Boolean Filter 1: Single Condition (High-Income Economies where GDP > $40,000)
high_income = df[df['GDP_per_Capita_USD'] > 40000]

print("\n--- Filtered: High-Income Economies (GDP > $40k) ---")
print(high_income)

# 3. Boolean Filter 2: Multiple Conditions (High Inflation AND Low GDP - Vulnerable Economies)
# Note: In Pandas, use parentheses () around each condition and '&' for AND, '|' for OR
vulnerable_economies = df[(df['Inflation_Rate_Pct'] > 5.0) & (
    df['GDP_per_Capita_USD'] < 15000)]

print("\n--- Filtered: Vulnerable Economies (Inflation > 5% & GDP < $15k) ---")
print(vulnerable_economies)
