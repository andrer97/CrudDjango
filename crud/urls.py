from django.contrib import admin
from django.urls import path, include
from .views import home, create, criar, editar, atualizar, update, deletar, delete  

urlpatterns = [
    path('', home, name="home"),
    path('create', create, name="create"),
    path('criar', criar, name="criar"),
    path('editar/<int:id>', editar, name="editar"),
    path('atualizar', atualizar, name="atualizar"),
    path('update/<int:id>', update, name="update"),
    path('deletar', deletar, name="deletar"),
    path('delete/<int:id>', delete, name="delete"),
]
