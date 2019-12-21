
from django.urls import path
from . import views

urlpatterns = [
    path('', views.DailyFixture ,name="DailyFix")
]
