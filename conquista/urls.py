from django.contrib import admin
from django.urls import path

from conquista import views

app_name = 'conquista'

urlpatterns = [
    path('', views.index, name="index"),
]