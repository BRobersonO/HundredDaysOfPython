import requests
import os
from dotenv import load_dotenv

load_dotenv()

WEATHER_ENDPOINT = "https://api.openweathermap.org/data/2.5/weather"
weather_params = {
    "lon": os.getenv('LONG'),
    "lat": os.getenv('LAT'),
    "appid": os.getenv('WEATHER_API'),
}


response = requests.get(WEATHER_ENDPOINT, params=weather_params)
response.raise_for_status()
weather_data = response.json()
ids = [dict['id'] for dict in weather_data['weather'] if dict['id'] < 700]
msg = "Bring an umbrella" if len(ids) > 0 else "No umbrella needed"
print(msg)
