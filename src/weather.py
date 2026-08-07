import os
import requests
WEATHER_API_KEY= os.getenv ("WEATHER_API_KEY","")
GEOCODE_URL = "https://geocoding-api.open-meteo.com/v1/search"
FORECAST_URL = "https://api.open-meteo.com/v1/forecast"

def get_cordinate(city):
    """"""
    response= requests.get(GEOCODE_URL,params={"name":city,"count":1},timeout=10)
    print(response.text)
get_cordinate("kathmandu")
cord=get_cordinate
print(cord[0])


# how api works
# what are api response status codes

