import requests
from datetime import datetime as dt
import os
from dotenv import load_dotenv

load_dotenv()
LONG = os.getenv('LONG')
LAT = os.getenv('LAT')

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()

# data = response.json()

# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]

# iss_position = (longitude, latitude)

# print(iss_position)

# Sunrise/Sunset

parameters = {
    "lat": LAT,
    "lng": LONG,
    "formatted": 0,
}
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)
time_now = dt.now().hour
print(time_now)