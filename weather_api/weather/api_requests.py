from dotenv import load_dotenv
import os
import requests
import json
from datetime import datetime

def get_weather(city, country):
    load_dotenv()

    api_key = os.environ.get('WEATHER_SECRET_APIKEY')
    if not api_key:
        raise ValueError("No API key found in environment variables")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={api_key}&mode=json"
    response = requests.get(url)


    if response.status_code != 200:
        return {'error': 'Failed to retrieve data from the weather service.'}

    try:
        print("Response content:", response.content.decode('utf-8'))
        weather_data = response.json()

    except json.JSONDecodeError as e:
        return {'error': f'Failed to parse weather data: {str(e)}'}

    location_name = f"{weather_data['name']}, {weather_data['sys']['country']}"

    temp_kelvin = weather_data['main']['temp']
    temp_celsius = temp_kelvin - 273.15
    temp_fahrenheit = (temp_celsius * 9/5) + 32

    wind_speed = weather_data['wind']['speed']
    wind_deg = weather_data['wind']['deg'] 
    wind_direction = "N/A"
    if wind_deg is not None:
        if 0 <= wind_deg <= 45 or 315 <= wind_deg <= 360:
            wind_direction = "North"
        elif 45 < wind_deg <= 135:
            wind_direction = "East"
        elif 135 < wind_deg <= 225:
            wind_direction = "South"
        elif 225 < wind_deg < 315:
            wind_direction = "West"

    cloudiness = weather_data['clouds']['all']  
    pressure = weather_data['main']['pressure']
    humidity = weather_data['main']['humidity']

    sunrise_ts = weather_data['sys']['sunrise']
    sunset_ts = weather_data['sys']['sunset']
    sunrise = datetime.fromtimestamp(sunrise_ts).strftime('%H:%M:%S')
    sunset = datetime.fromtimestamp(sunset_ts).strftime('%H:%M:%S')

    coord_lat = weather_data['coord']['lat']
    coord_lon = weather_data['coord']['lon']

    last_update_ts = weather_data['dt']  
    requested_time = datetime.fromtimestamp(last_update_ts).strftime('%Y-%m-%d %H:%M:%S')

    weather_dict = {
        'location_name': location_name,
        'temperature': f"{temp_celsius:.2f}°C, {temp_fahrenheit:.2f}°F",
        'wind': f"{wind_speed} m/s, {wind_direction}",
        'cloudiness': f"{cloudiness}%",
        'pressure': f"{pressure} hPa",
        'humidity': f"{humidity}%",
        'sunrise': sunrise,
        'sunset': sunset,
        'geo_coordinates': f"[{coord_lat}, {coord_lon}]",
        'requested_time': requested_time
    }

    return weather_dict