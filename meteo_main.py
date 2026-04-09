import requests

API_KEY = "ff7b3a1640a9ca14d9cc295afc1bed1e"  
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
VILLE = "Dakar"

params = {
    "q": VILLE,
    "appid": API_KEY,
    "units": "metric",
    "lang": "fr"
}

response = requests.get(BASE_URL, params=params)

if response.status_code == 200:
    data = response.json()
    print("Temperature :", data["main"]["temp"], "°C")
    print("Conditions :", data["weather"][0]["description"])
    print("Humidite :", data["main"]["humidity"], "%")
else:
    print("Erreur :", response.status_code, response.text)
