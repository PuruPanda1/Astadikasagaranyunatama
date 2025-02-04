from django.conf import settings
from server.utils.point import Point
import requests
from server.utils.tools import average_height
from datetime import datetime

def get_location_parameters(point: Point, use_tide_api: bool):
    open_weather_data = get_open_weather_data(point)
    if use_tide_api:
        tide_data = get_world_tide_data(point)
    else:
        tide_data = 0
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
   

    url = f"{settings.WORLD_TIDE_BASE_URL}&lat={lat}&lon={long}&date={datetime.now().strftime('%Y-%m-%d')}&key={settings.WORLD_TIDE_API_KEY}"

    response = requests.get(url)
    
    json_data = response.json()
    
    # Extracting the tide heights

    if(json_data["status"] == 400):
        return 0
    heights = [entry["height"] for entry in json_data["heights"]]
    
    avg_height = average_height(heights)
    
    return avg_height

# * TESTING THE FUNCTION
# get_open_weather_data(Point(latitude=7.367, longitude=45.133))

