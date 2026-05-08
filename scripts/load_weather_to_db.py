import os
import requests
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

engine = create_engine(
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

CITY = "Boston"

url = f"https://wttr.in/{CITY}?format=j1"

response = requests.get(url)
data = response.json()

current = data["current_condition"][0]

weather_data = {
    "city": CITY,
    "temperature_c": float(current["temp_C"]),
    "humidity": int(current["humidity"]),
    "weather_desc": current["weatherDesc"][0]["value"],
    "observation_time": datetime.now()
}

df = pd.DataFrame([weather_data])

df.to_sql(
    "raw_weather",
    engine,
    if_exists="append",
    index=False
)

print("Weather data inserted successfully!")
print(df)