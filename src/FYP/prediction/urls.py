from django.urls import path
from . import views

urlpatterns = [
    path('', views.matchPred, name ="pred"),
]