import requests

APIKEY = "***REMOVED***"
LAT = 38
LON = -77

response = requests.get("https://api.openweathermap.org/data/2.5/weather?lat=***REMOVED***&lon=***REMOVED***&appid=***REMOVED***")