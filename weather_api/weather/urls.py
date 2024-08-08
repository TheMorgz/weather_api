from django.urls import path
from weather import views

urlpatterns = [
    path(
        route='weather/<str:city>/<str:country>/',
        view=views.weather_detail,
        name='weather_detail'
    ),
]