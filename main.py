import requests

api_key = "22601981ba72110106b746ab63b7655d"
url_forecast = "https://api.openweathermap.org/data/2.5/forecast"

parameters = {
    "lat":  -34.603683,
    "lon": -58.381557,
    "appid": api_key,
    "cnt": 3
}

response = requests.get(url=url_forecast, params=parameters)
response.raise_for_status()
weather_data = response.json()

will_rain = False

for hour_data in weather_data["list"]:
    condition_code = print(hour_data["weather"][0]["id"])
    if int(condition_code) < 700: 
        will_rain = True
        
if will_rain:
    print("Bring an umbrella!")
    
