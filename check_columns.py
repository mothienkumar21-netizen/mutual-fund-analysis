import pandas as pd

files = [
    "data/raw/02_nav_history.csv",
    "data/raw/08_investor_transactions.csv",
    "data/raw/07_scheme_performance.csv"
]

for file in files:
    df = pd.read_csv(file)
    print("\n" + "="*50)
    print(file)
    print(df.columns.tolist())