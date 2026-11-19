# Economic Data Science Portfolio: MIT 6.0002

## Lecture 1: Greedy Heuristic FPL Optimizer
* **Concept:** Implemented a greedy heuristic for the 0/1 Knapsack problem using a custom Python class and data structures to select an optimal Fantasy Premier League squad.
* **Key Finding:** Discovered local-optimum trapping where the algorithm left 35% of the budget unspent (£48.5m spent out of £75.0m) due to myopic, step-by-step decision-making based purely on value density (points-per-million).
* **Live Demo:** [Run this notebook live in Google Colab](https://colab.research.google.com/github/paninibot/economic-data-science-portfolio/blob/main/MIT_60002_Lecture1_FPL_Optimizer.ipynb)

## Lecture 2: Search Tree (Decision Tree) FPL Optimizer
* **Concept:** Built a recursive search tree (`Take` vs. `Leave` branches) to evaluate squad combinations globally under a £75.0m budget and 8-player cap.
* **Key Finding:** Outperformed the greedy heuristic by +230 points (1450 vs. 1220) by utilizing the full £75.0m budget instead of stopping at £61.0m[cite: 10].
* **Trade-Off & Next Step:** Pure search trees grow exponentially (~2^n branches) as the player pool expands, motivating dynamic programming (memoization) to avoid recomputing overlapping states.
* **Live Demo:** [Run this notebook live in Google Colab](https://colab.research.google.com/github/paninibot/economic-data-science-portfolio/blob/main/MIT_60002_Lecture2_SearchTree_FPL.ipynb)
