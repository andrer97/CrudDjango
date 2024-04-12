from django.contrib import admin
from django.urls import path, include
from .views import home, criar, editar, atualizar, deletar

urlpatterns = [
    path('', home),
    path('criar', criar, name="criar"),
    path('editar/<int:id>', editar, name="editar"),
    path('atualizar/<int:id>', atualizar, name="atualizar"),
    path('deletar/<int:id>', deletar, name="deletar"),
]
