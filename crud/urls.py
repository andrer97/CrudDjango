from django.contrib import admin
from django.urls import path, include
from .views import home, criar, atualizar

urlpatterns = [
    path('', home),
    path('criar', criar, name="criar"),
    path('atualizar/<int:id>', atualizar, name="atualizar")
]
