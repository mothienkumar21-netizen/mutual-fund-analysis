import pandas as pd
import os

DATA_PATH = "data/raw"
csv_files = [file for file in os.listdir(DATA_PATH) if file.endswith(".csv")]

print(f"\nFound {len(csv_files)} CSV files\n")

for file in csv_files:

    print("=" * 60)
    print(f"Dataset: {file}")

    filepath = os.path.join(DATA_PATH, file)

    try:
        df = pd.read_csv(filepath)

        print("\nShape:")
        print(df.shape)

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nDuplicate Rows:")
        print(df.duplicated().sum())

        print("\n")

    except Exception as e:
        print(f"Error loading {file}: {e}")


if "fund_master.csv" in csv_files and "nav_history.csv" in csv_files:

    print("\n==============================")
    print("AMFI CODE VALIDATION")
    print("==============================\n")

    fund_master = pd.read_csv(os.path.join(DATA_PATH, "fund_master.csv"))
    nav_history = pd.read_csv(os.path.join(DATA_PATH, "nav_history.csv"))

    master_codes = set(fund_master["scheme_code"].unique())
    nav_codes = set(nav_history["scheme_code"].unique())

    missing_codes = master_codes - nav_codes

    print(f"Total fund_master codes: {len(master_codes)}")
    print(f"Total nav_history codes: {len(nav_codes)}")
    print(f"Missing codes in nav_history: {len(missing_codes)}")

    if len(missing_codes) > 0:
        print("\nMissing Codes:")
        print(list(missing_codes)[:20])

    print("\nData Quality Summary:")
    print("- Checked AMFI code consistency")
    print("- Verified NAV history mapping")