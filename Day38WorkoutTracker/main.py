import requests
import os
from dotenv import load_dotenv
from datetime import datetime

NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = "https://api.sheety.co/b2a139232bc08d5f0eb12750793493c8/workoutTrackerDemo/workouts"
SHEETY_TOKEN = os.getenv('SHEETY_WORKOUT')

load_dotenv()

headers = {
    "x-app-key": os.getenv('NUTRITIONIX_API'),
    "x-app-id": os.getenv('NUTRITIONIX_APP_ID'),
}
my_input = input("What exercise did you do? ")
requests_params = {
    "query":my_input,
}

response = requests.post(NUTRITIONIX_ENDPOINT, json=requests_params, headers=headers)
exercises = response.json()

sheety_header = {
    "Authorization": f"Bearer {SHEETY_TOKEN}"
}

date = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%X")

for exercise in exercises["exercises"]:
    test_body = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }
    sheety_response = requests.post(SHEETY_ENDPOINT, json=test_body, headers=sheety_header)
    print(sheety_response.text)

# sheet link: https://docs.google.com/spreadsheets/d/134imVQ5eNhAaiWbnKjDG4MXhXQGdLHqL_uAapSZkDY0/edit#gid=0