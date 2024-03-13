"""
URL configuration for flight_reservation project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from .views import flights,flight, passengers, passenger, reservations, reservation, find_flight,reserveFlight
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('flights', flights.as_view()),
    path('flights/<int:pk>', flight.as_view()),
    path('passengers', passengers.as_view()),
    path('passengers/<int:pk>', passenger.as_view()),
    path('reservations', reservations.as_view()),
    path('reservations/<int:pk>', reservation.as_view()),
    path('findFlights', find_flight),
    path('reserveFlight', reserveFlight),
    path('authenticate', obtain_auth_token, name="api_token_auth"),

]
