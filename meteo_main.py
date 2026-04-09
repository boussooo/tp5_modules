import requests

API_KEY = "TA_CLE_API"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
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
    print("Température :", data["main"]["temp"], "°C")
    print("Description :", data["weather"][0]["description"])
    print("Humidité :", data["main"]["humidity"], "%")
else:
    print("Erreur :", response.status_code)