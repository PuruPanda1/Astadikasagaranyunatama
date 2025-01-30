import openmeteo_requests
import requests_cache
from retry_requests import retry
from django.conf import settings
from server.utils.point import Point
import requests
from server.utils.tools import average_height
import asyncio

cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)

url = settings.BASE_URL
parameter = ["wave_height_max", "wave_period_max", "wind_wave_height_max", "wind_wave_period_max", "swell_wave_height_max", "swell_wave_period_max"]

# TODO World Tide API parameters
# &date=2024-12-09&lat=33.768321&lon=-118.195617&key=

# TODO Open Weather API parameters  
# ?lat=33.44&lon=-94.04&exclude=hourly,daily&appid={API key}

def get_data(point: Point):
    lat = point.latitude
    long = point.longitude
    params = {
        "latitude": lat,
        "longitude": long,
        "daily": parameter,
        "forecast_days": 1,
        "timezone": settings.TIME_ZONE
    }

    responses = openmeteo.weather_api(url, params=params)

    response = responses[0]
    # print(f"Coordinates {response.Latitude()}°N {response.Longitude()}°E")
    # print(f"Elevation {response.Elevation()} m asl")
    # print(f"Timezone {response.Timezone()} {response.TimezoneAbbreviation()}")
    # print(f"Timezone difference to GMT+0 {response.UtcOffsetSeconds()} s")

    daily = response.Daily()
    daily_wave_height_max = daily.Variables(0).ValuesAsNumpy()
    daily_wave_period_max = daily.Variables(1).ValuesAsNumpy()
    daily_wind_wave_height_max = daily.Variables(2).ValuesAsNumpy()
    daily_wind_wave_period_max = daily.Variables(3).ValuesAsNumpy()
    daily_swell_wave_height_max = daily.Variables(4).ValuesAsNumpy()
    daily_swell_wave_period_max = daily.Variables(5).ValuesAsNumpy()

    return {'height': daily_wave_height_max, 'period': daily_wave_period_max}

def get_location_parameters(point: Point):
    open_weather_data = get_open_weather_data(point)
    tide_data = get_world_tide_data(point)
    print(f'Point {point.latitude} & {point.longitude} api data ---> {open_weather_data}')
    return {
        'wind_speed': open_weather_data['wind_speed'],
        'weather_description': open_weather_data['weather_description'],
        'visibility': open_weather_data['visibility'],
        'sea_level': open_weather_data['sea_level'],
        'tide_height': tide_data
    }

def get_open_weather_data(point: Point):
    lat = point.latitude
    long = point.longitude
    params = {
        "lat": lat,
        "lon": long,
        "exclude": "hourly,daily",
        "appid": settings.OPEN_WEATHER_API_KEY
    }

    url = f"{settings.OPEN_WEATHER_BASE_URL}?lat={lat}&lon={long}&exclude=hourly,daily&appid={settings.OPEN_WEATHER_API_KEY}"

    response = requests.get(url)
    
    json_data = response.json()
    
    # Extracting required data
    wind_data = json_data.get('wind', {})
    wind_speed = wind_data.get('speed', 'No wind speed data')
    weather_description = json_data.get('weather', [{}])[0].get('description', 'No description available')
    visibility = json_data.get('visibility', 'No visibility data')
    sea_level = json_data.get('main', {}).get('sea_level', 'No sea level data')

    
    return {
        'wind_speed': wind_speed,
        'weather_description': weather_description,
        'visibility': visibility,
        'sea_level': sea_level
        }

def get_world_tide_data(point: Point):
    lat = point.latitude
    long = point.longitude
   

    url = f"{settings.WORLD_TIDE_BASE_URL}?date=2024-12-09&lat={lat}&lon={long}&key={settings.WORLD_TIDE_API_KEY}"

    response = requests.get(url)
    
    json_data = response.json()
    
    print(json_data)
    # Extracting the tide heights

    if(json_data["status"] == 400):
        return "No tide height data available"
    heights = [entry["height"] for entry in json_data["heights"]]
    
    avg_height = average_height(heights)
    
    return avg_height

# * TESTING THE FUNCTION
# get_open_weather_data(Point(latitude=7.367, longitude=45.133))

