import matplotlib.pyplot as plt

# 1. Define our economic data (Years and corresponding GDP Growth Rate %)
years = [2019, 2020, 2021, 2022, 2023]
gdp_growth = [1.8, -3.4, 5.5, 2.1, 2.5]

# 2. Initialize the Figure and Axes (The Canvas and the Plot Box)
fig, ax = plt.subplots(figsize=(8, 5))

# 3. Plot the data as a line chart with markers
ax.plot(years, gdp_growth, color='teal', linewidth=2.5,
        marker='o', label='Real GDP Growth (%)')

# 4. Add structural economic labels and title
ax.set_title('Macroeconomic Recovery Post-2020',
             fontsize=14, fontweight='bold')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('GDP Growth Rate (%)', fontsize=12)

# 5. Add a horizontal line at 0% to clearly show recessions (negative growth)
ax.axhline(0, color='red', linestyle='--', linewidth=1,
           label='Recession Threshold (0%)')

# 6. Add a legend and grid for readability
ax.legend(loc='upper left')
ax.grid(True, linestyle=':', alpha=0.6)

# 7. Render the visualization window
plt.tight_layout()
plt.show()
