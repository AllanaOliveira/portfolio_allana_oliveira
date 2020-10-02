from django.contrib import admin
from django.urls import path

from pais import views

app_name = 'pais'

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:id>', views.show, name="show"),
]