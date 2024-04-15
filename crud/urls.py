from django.contrib import admin
from django.urls import path
from .views import home, pesquisar, criar, editar, atualizar, deletar  

urlpatterns = [
    path('', home, name="home"),
    path('pesquisar', pesquisar, name="pesquisar"),
    path('criar', criar, name="criar"),
    path('editar/<int:id>', editar, name="editar"),
    path('atualizar', atualizar, name="atualizar"),
    path('deletar/', deletar, name="deletar"),
    path('deletar/<int:id>', deletar, name="deletar"),
]
