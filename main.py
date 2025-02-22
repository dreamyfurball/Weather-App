import os
import requests
from twilio.rest import Client
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Secure API Credentials
api_key = os.getenv("API_KEY")
account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.getenv("AUTH_TOKEN")
twilio_phone = os.getenv("TWILIO_PHONE")
recipient_phone = os.getenv("RECIPIENT_PHONE")

LAT = 37.971558
LONG = -87.571091

parameters = {
    "lat": LAT,
    "lon": LONG,
    "appid": api_key,
    "cnt": 4
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
data = response.json()

will_rain = False
for i in range(0, 4):
    weather_code = data["list"][i]["weather"][0]["id"]
    if weather_code < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_=twilio_phone,
        body="Bring an umbrella ☂️",
        to=recipient_phone
    )
    print(message.status)

