import pandas as pd 
import json
import os 
from datetime import datetime

os.makedirs("processed_data", exist_ok= True)

today = datetime.now().strftime("%Y-%m-%d")

def transform_exchange_rate():
    with open("raw_data/exchange_rate.json","r") as f:
        data = json.load(f)
    
    ngn_rate = data["rates"]["NGN"]
    base = data["base"]
    date = data["date"]

    df = pd.DataFrame([{
        "base_currency": base,
        "target_currency": "NGN",
        "rate": ngn_rate,
        "date": date,
        "date_extracted": today
    }])

    df.to_csv("processed_data/exchange_rate.csv", index = False)
    print("Exchange rate transformed successfully")
    print(df)

def transform_inflation():
    with open("raw_data/inflation.json", "r") as f:
        data = json.load(f)

    records = []
    for entry in data[1]:
        if entry["value"] is not None:
            records.append({
                "country": entry["country"]["value"],
                "year": entry["date"],
                "inflation_rate": round(entry["value"], 2),
                "date_extracted" : today    
            })
    
    df = pd.DataFrame(records)
    df = df.sort_values("year", ascending=True).reset_index(drop = True)

    df.to_csv("processed_data/inflation.csv", index=False)
    print("Inflation data transformed successfully")
    print(df)

def tranform_oil_prices():
    with open("raw_data/oil_prices.json", "r") as f:
        data =json.load(f)

    records = []
    for entry in data[1]:
        if entry["value"] is not None:
            records.append({
                "country": entry["country"]["value"],
                "year": entry["date"],
                "gdp_usd":round(entry["value"], 2),
                "date_extracted" : today

            })
    df = pd.DataFrame(records)
    df = df.sort_values("year", ascending=True).reset_index(drop = True)
    
    df.to_csv("processed_data/gdp.csv", index = False)

    print("GDP data transformed successfully")
    print(df)

if __name__ == "__main__":
    print("Starting transformation...")
    print(f"Tine: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-"*40)

    transform_exchange_rate()
    transform_inflation()
    tranform_oil_prices()

    print("-"* 40)
    print("Transformation Complete!")

    