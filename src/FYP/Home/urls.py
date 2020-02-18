#---- Home urls.py

from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Home, name = "HomePage"),
]
