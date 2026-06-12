import pandas as pd
import os

RAW = "data/raw"
PROCESSED = "data/processed"

os.makedirs(PROCESSED, exist_ok=True)

# ------------------
# NAV HISTORY
# ------------------
nav = pd.read_csv(f"{RAW}/02_nav_history.csv")

nav["date"] = pd.to_datetime(nav["date"])

nav = nav.sort_values(["amfi_code", "date"])

nav["nav"] = nav.groupby("amfi_code")["nav"].ffill()

nav = nav.drop_duplicates()

nav = nav[nav["nav"] > 0]

nav.to_csv(f"{PROCESSED}/02_nav_history_clean.csv", index=False)

print("NAV cleaned")


# ------------------
# INVESTOR TRANSACTIONS
# ------------------
txn = pd.read_csv(f"{RAW}/08_investor_transactions.csv")

txn["transaction_date"] = pd.to_datetime(
    txn["transaction_date"],
    errors="coerce"
)

txn["transaction_type"] = (
    txn["transaction_type"]
    .str.strip()
    .str.title()
)

txn["transaction_type"] = txn["transaction_type"].replace({
    "Sip": "SIP",
    "Lumpsum": "Lumpsum",
    "Redemption": "Redemption"
})

txn = txn[txn["amount_inr"] > 0]

valid_kyc = ["Verified", "Pending", "Rejected"]

txn["kyc_valid"] = txn["kyc_status"].isin(valid_kyc)

txn.to_csv(
    f"{PROCESSED}/08_investor_transactions_clean.csv",
    index=False
)

print("Transactions cleaned")


# ------------------
# SCHEME PERFORMANCE
# ------------------
perf = pd.read_csv(
    f"{RAW}/07_scheme_performance.csv"
)

return_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

for col in return_cols:
    perf[col] = pd.to_numeric(
        perf[col],
        errors="coerce"
    )

perf["expense_valid"] = (
    perf["expense_ratio_pct"]
    .between(0.1, 2.5)
)

perf.to_csv(
    f"{PROCESSED}/07_scheme_performance_clean.csv",
    index=False
)

print("Performance cleaned")

print("\nAll cleaning complete.")