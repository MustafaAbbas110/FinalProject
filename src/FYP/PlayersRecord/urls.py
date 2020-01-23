from django.urls import path
from . import views

urlpatterns = [
    path('', views.PlayersRecord, name ="pRec"),
]