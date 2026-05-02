import requests
import os 
import json
from datetime import datetime 

os.makedirs("raw_data", exist_ok=True)

def fetch_exchange_rate():
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        with open("raw_data/exchange_rate.json", "w") as f:
            json.dump(data, f, indent = 4)
        print("Exchange rate data saved successfully")
    else:
        print("Failed to fetch exchange rate:",response.status_code)

def fetch_inflation():
    url = "https://api.worldbank.org/v2/country/NG/indicator/FP.CPI.TOTL.ZG?format=json&mrv=10"
    response =requests.get(url)

    if response.status_code == 200:
        data = response.json()
        with open("raw_data/inflation.json", "w") as f:
            json.dump(data, f, indent=4)
        print("Inflation data saved Successfully")
    else:
        print("Failed to fetch inflation data:", response.status_code)

def fetch_oil_prices():
    url = "https://api.worldbank.org/v2/country/NG/indicator/NY.GDP.MKTP.CD?format=json&mrv=10"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        with open("raw_data/oil_prices.json", "w") as f:
            json.dump(data, f, indent=4)
        print("Oil prices data saved successfully")
    else:
        print("Failed to fetch oil prices:", response.status_code)

if __name__ == "__main__":
    print("Starting Extraction...")
    print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 40)

    fetch_exchange_rate()
    fetch_inflation()
    fetch_oil_prices()

    print("-" *40)
    print("Extraction complete!")


