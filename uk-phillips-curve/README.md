# Empirical Analysis of the UK Phillips Curve (2015–2026)

## 📌 Project Overview
An independent data science portfolio project investigating whether the traditional macroeconomic relationship between UK unemployment and wage growth (the Phillips Curve) experienced structural breaks following post-pandemic economic shocks.

## 🛠️ Tech Stack & Tools
* **Language:** Python (executed via Google Colab)
* **Libraries:** `pandas` (Data manipulation & time-series cleaning), `matplotlib` / `seaborn` (Data visualization), `statsmodels` (Econometric OLS regression modeling)
* **Data Source:** Official Office for National Statistics (ONS) Time Series Datasets (`MGSX` & `KAC3`)

## 📂 Repository Contents
* `UK_Phillips_Curve_Analysis.ipynb`: The core Jupyter notebook containing data ingestion, ONS metadata header skipping, date indexing, regression modeling, and visual scatter plots.

## 📊 Key Economic & Data Science Takeaways
* **Data Wrangling:** Cleaned raw ONS government datasets by handling metadata offset rows and parsing monthly time-series indices.
* **Econometric Analysis:** Modeled labor market trade-offs using Ordinary Least Squares (OLS) regression to quantify the sensitivity of wage growth to shifts in unemployment.
* **Critical Evaluation:** Highlighted how global supply-chain shocks and inflation spikes alter standard macroeconomic curves, demonstrating the value of combining quantitative programming with economic theory.