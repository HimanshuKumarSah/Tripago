from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name=""),
    path('register.html', views.register, name="register"),
    path('login.html', views.login, name="login"),
    path('dashboard.html', views.dashboard, name="dashboard"),
    path('logout.html', views.logout, name="logout"),
    path('create-itinerary.html', views.create_itinerary, name="create-itinerary"),
]