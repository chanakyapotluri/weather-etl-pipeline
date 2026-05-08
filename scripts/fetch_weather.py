import requests
import pandas as pd
from datetime import datetime
import os

CITY = "Boston"

url = f"https://wttr.in/{CITY}?format=j1"

response = requests.get(url)
data = response.json()

current = data["current_condition"][0]

weather_data = {
    "city": CITY,
    "temperature_C": current["temp_C"],
    "humidity": current["humidity"],
    "weather_desc": current["weatherDesc"][0]["value"],
    "observation_time": datetime.now()
}

df = pd.DataFrame([weather_data])

os.makedirs("data/raw", exist_ok=True)

file_name = f"data/raw/weather_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

df.to_csv(file_name, index=False)

print("Weather data saved successfully!")
print(file_name)
print(df)