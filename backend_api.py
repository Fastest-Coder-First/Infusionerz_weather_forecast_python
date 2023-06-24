import requests
import pandas as pd
from datetime import datetime

from fastapi import FastAPI

app = FastAPI()

api_key = "3459c76112365553fd50982219f5ae7a"  # API key

def convert_to_celsius_and_round_off(kelvin_temp):
    """
    Converts temperature from Kelvin to Celsius and rounds off to 2 decimal places.
    """
    celsius_temp = kelvin_temp - 273.15
    return round(celsius_temp, 2)

@app.get("/weather")
def get_weather(city_name: str, country_code: str):
    """
    Retrieves weather data for a specified location using OpenWeatherMap API.
    """
    # Get city details (latitude and longitude) from OpenWeatherMap Geocoding API
    get_city_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},{country_code}&limit=1&appid={api_key}"
    city_details = requests.get(get_city_url).json()[0]

    lat = city_details['lat']
    lon = city_details['lon']

    # Create the URL for weather data retrieval
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"

    # Send request to the API
    response = requests.get(url)

    data = response.json()
    weather_data = {
        "latitude": lat,
        "longitude": lon,
        "temperature": convert_to_celsius_and_round_off(data["main"]["temp"]),
        "temp_min": convert_to_celsius_and_round_off(data["main"]["temp_min"]),
        "temp_max": convert_to_celsius_and_round_off(data["main"]["temp_max"]),
        "humidity": data["main"]["humidity"],
        "description": data["weather"][0]["description"],
        "visibility": data["visibility"],
        "wind_speed": data["wind"]["speed"],
        "sunrisetime": datetime.utcfromtimestamp(data["sys"]["sunrise"]).time(),
        "sunsettime": datetime.utcfromtimestamp(data["sys"]["sunset"]).time(),
    }
    return weather_data