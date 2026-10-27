import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Macroeconomic panel dataset for distributional analysis
data = {
    'Country': ['USA', 'UK', 'Germany', 'Japan', 'France', 'Brazil', 'India', 'Nigeria', 'Argentina', 'South Africa'],
    'Continent': ['North America', 'Europe', 'Europe', 'Asia', 'Europe', 'South America', 'Asia', 'Africa', 'South America', 'Africa'],
    'GDP_per_Capita_USD': [76000, 46000, 51000, 39000, 44000, 89000, 2300, 2100, 13000, 6700]
}

df = pd.DataFrame(data)

print("--- Economic Panel Dataset Loaded ---")
print(df)

# 2. Set Seaborn visual aesthetic theme
sns.set_theme(style="whitegrid")

# 3. Create a multi-panel figure for distributional auditing
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Plot A: Combined Histogram and Kernel Density Estimate (KDE)
sns.histplot(df['GDP_per_Capita_USD'], kde=True, ax=axes[0], color='royalblue')
axes[0].set_title('Global GDP per Capita Distribution (Histogram & KDE)')
axes[0].set_xlabel('GDP per Capita (USD)')
axes[0].set_ylabel('Frequency')

# Plot B: Categorical Boxplot with Individual Data Points (Stripplot overlay)
sns.boxplot(data=df, x='Continent', y='GDP_per_Capita_USD',
            ax=axes[1], palette='Set3', boxprops=dict(alpha=0.8))
sns.stripplot(data=df, x='Continent', y='GDP_per_Capita_USD',
              ax=axes[1], color='black', size=5, jitter=0.2, alpha=0.7)
axes[1].set_title('GDP per Capita Spread by Continent')
axes[1].set_xlabel('Continent')
axes[1].set_ylabel('GDP per Capita (USD)')

# Adjust layout for readability and render figures
plt.tight_layout()
plt.show()
