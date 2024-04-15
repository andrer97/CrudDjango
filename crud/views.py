from django.shortcuts import render, redirect
import re
from .models import Usuario

# Create your views here.

def home(request):
    usuarios = Usuario.objects.all()
    return render(request, "crud/global/index.html", {"usuarios": usuarios})

def pesquisar(request):
    if request.POST:
        nome_filtro = request.POST.get("nome")
        usuarios = Usuario.objects.filter(nome__icontains=nome_filtro)
    else:
        usuarios = Usuario.objects.all()

    return render(request, "crud/global/pesquisar.html", {"usuarios": usuarios})

def criar(request):
    if request.POST:
        nome = request.POST.get("nome")
        dataNascimento = request.POST.get("dataNascimento")
        email = request.POST.get("email")
        paisDestino = request.POST.get("paisDestino")
        Usuario.objects.create(nome=nome, dataNascimento=dataNascimento, email=email, paisDestino=paisDestino)

    return render(request, "crud/global/criar.html")

def editar(request, id):
    if request.POST:
        nome = request.POST.get("nome")
        dataNascimento = request.POST.get("dataNascimento")
        email = request.POST.get("email")
        paisDestino = request.POST.get("paisDestino")
        usuario = Usuario.objects.get(id=id)
        usuario.nome = nome
        usuario.dataNascimento = dataNascimento
        usuario.email = email
        usuario.paisDestino = paisDestino
        usuario.save()
        return redirect(atualizar)
    else:
        usuario = Usuario.objects.get(id=id)
        return render(request, "crud/global/editar.html", {"usuario": usuario})

def atualizar(request):
    if request.POST:
        nome_filtro = request.POST.get("nome")
        usuarios = Usuario.objects.filter(nome__icontains=nome_filtro)
    else:
        usuarios = Usuario.objects.all()
    return render(request, "crud/global/atualizar.html", {"usuarios": usuarios})

def deletar(request, id=None):
    if request.POST:
        nome_filtro = request.POST.get("nome")
        usuarios = Usuario.objects.filter(nome__icontains=nome_filtro)
    else:
        if id:
            usuario = Usuario.objects.get(id=id)
            usuario.delete()
        usuarios = Usuario.objects.all()
    return render(request, "crud/global/deletar.html", {"usuarios": usuarios})