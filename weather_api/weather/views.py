# Django
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Serializers
from .serializers import WeatherSerializer

# Utilities
from .api_requests import get_weather

# Cache
from django.core.cache import cache


@api_view(['GET'])
def weather_detail(request, city, country):
    """Receive the client request and return a JSON 
    response with the given city and country."""
    
    data = {'city': city, 'country': country}
    serializer = WeatherSerializer(data=data)
    
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    country = serializer.validated_data['country']
    city = serializer.validated_data['city']
    
    cache_key = f"{country}-{city}"
    
    if cache_data := cache.get(cache_key):
        return Response(cache_data)
    
    weather_data = get_weather(city, country)
    
    cache.set(cache_key, weather_data, timeout=60*2)
    
    return Response(weather_data)