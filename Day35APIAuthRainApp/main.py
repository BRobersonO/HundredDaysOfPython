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
print(response.status_code)