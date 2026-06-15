# Mutual Fund Analytics Data Dictionary

## 02_nav_history.csv

| Column | Type | Description |
|----------|----------|----------|
| amfi_code | Integer | Unique mutual fund code |
| date | Date | NAV date |
| nav | Float | Net Asset Value |

---

## 08_investor_transactions.csv

| Column | Type | Description |
|----------|----------|----------|
| investor_id | Integer | Investor ID |
| transaction_date | Date | Transaction date |
| amfi_code | Integer | Fund code |
| transaction_type | Text | SIP/Lumpsum/Redemption |
| amount_inr | Float | Transaction amount |
| state | Text | Investor state |
| city | Text | Investor city |
| kyc_status | Text | KYC verification status |

---

## 07_scheme_performance.csv

| Column | Type | Description |
|----------|----------|----------|
| scheme_name | Text | Fund name |
| fund_house | Text | AMC name |
| category | Text | Fund category |
| return_1yr_pct | Float | 1-year return |
| return_3yr_pct | Float | 3-year return |
| return_5yr_pct | Float | 5-year return |
| sharpe_ratio | Float | Risk-adjusted return |
| expense_ratio_pct | Float | Expense ratio |
| aum_crore | Float | Assets under management |
| risk_grade | Text | Risk classification |