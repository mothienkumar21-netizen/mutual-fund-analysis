import requests
import pandas as pd
import os

# Create output folder
os.makedirs("data/raw/live_nav", exist_ok=True)

# Mutual fund schemes
schemes = {
    "HDFC_Top_100": 125497,
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_Large_Cap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

for fund_name, scheme_code in schemes.items():

    url = f"https://api.mfapi.in/mf/{scheme_code}"

    print(f"\nFetching NAV for {fund_name}")

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        meta = data.get("meta", {})
        nav_data = data.get("data", [])

        df = pd.DataFrame(nav_data)

        # Add metadata
        df["fund_name"] = meta.get("scheme_name")
        df["scheme_code"] = meta.get("scheme_code")
        df["fund_house"] = meta.get("fund_house")

        output_file = f"data/raw/live_nav/{fund_name}.csv"

        df.to_csv(output_file, index=False)

        print(f"Saved: {output_file}")

        print(df.head())

    else:
        print(f"Failed to fetch {fund_name}")