import numpy as np
import pandas as pd

# 1. Economic Data Matrix (3 Countries, 2 Metrics: [GDP per Capita in $k, Literacy Rate %])
X = np.array([
    [45.0, 0.98],  # Country A
    [12.0, 0.85],  # Country B
    [2.5, 0.60]   # Country C
])

print("--- Economic Data Matrix X (3x2) ---")
print(X)

# 2. Economic Policy Weights Vector (w)  70% weight on GDP, 30% on Literacy
w = np.array([0.7, 0.3])

# 3. Matrix Multiplication: Dot Product to compute composite health scores
scores = np.dot(X, w)

print("\n--- Weighted Economic Health Score Vector ---")
print(scores)

# 4. Bind back into a Pandas DataFrame
df_matrix = pd.DataFrame(X, columns=['GDP_k', 'Literacy'], index=[
                         'Country_A', 'Country_B', 'Country_C'])
df_matrix['Composite_Score'] = scores

print("\n--- Final Matrix-Processed DataFrame ---")
print(df_matrix)
