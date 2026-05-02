import pandas as pd 
import sqlite3
from  datetime import datetime

conn =  sqlite3.connect('nigeria_economy.db')
cursor = conn.cursor()

print("connected to database successfully")

def load_exchange_rate(): 
    df = pd.read_csv("Processed_data/exchange_rate.csv")
    df.to_sql("exchange_rate", conn, if_exists = "replace", index=False)
    print("Exchange rate loaded successfully")
    print(df)

def load_inflation():
    df = pd.read_csv("processed_data/inflation.csv")
    df.to_sql("inflation", conn, if_exists="replace", index= False )
    print("Inflation data Loaded successfully")
    print(df)

def load_gdp():
    df = pd.read_csv("processed_data/gdp.csv")
    df.to_sql("gdp", conn, if_exists="replace", index= False)
    print(df)

def verify_data():
    print("\n--- Verifying loaded data ---")
    
    for table in ["exchange_rate", "inflation", "gdp"]:
        cursor.execute(f'SELECT COUNT(*) FROM "{table}"')
        count = cursor.fetchone()[0]
        print(f"✅ Table '{table}': {count} row(s)")


if __name__ == "__main__":
    print("Loading Into SQL...")
    print(f" Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-"*40)

    load_exchange_rate()
    load_inflation()
    load_gdp()
    verify_data()

    conn.commit()
    conn.close()

    print("-"*40)
    print('Loading into SQL DOne!')
    

