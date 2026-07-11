import pandas as pd
import sys
sys.path.append("src")

from classifier import classify_portfolio
from calculations import calculate_risk_adjustment, calculate_csm_release
from report import print_summary, plot_charts

# Step 1 - Load data
print("Loading contract data")
df = pd.read_csv("data/contracts.csv")

# Step 2 - Classify contracts
df = classify_portfolio(df)

# Step 3 - Calculate risk adjustment and total liability
print("Calculating risk adjustments...")
df = calculate_risk_adjustment(df)

# Step 4 - Calculate CSM release
print("Calculating CSM release...")
df = calculate_csm_release(df)

# Step 5 - Print summary and charts
print_summary(df)
plot_charts(df)