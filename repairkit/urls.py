from django.urls import path
from .views import add_car, home, cars

urlpatterns = [
    path('add_car', add_car, name='add_car'),
    path('home', home, name="home"),
    path('cars', cars, name="cars")
]
