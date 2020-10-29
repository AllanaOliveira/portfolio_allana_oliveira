from django.contrib import admin
from django.urls import path

from palavra_vida import views

app_name = 'palavra_vida'

urlpatterns = [
    path('', views.index, name="index"),
    path('cadastra_motivacao/', views.cadastra_motivacao, name='cadastra_motivacao'),
]