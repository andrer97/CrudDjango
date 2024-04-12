from django.shortcuts import render, redirect
from .models import Usuario

# Create your views here.

def home(request):
    usuarios = Usuario.objects.all()
    return render(request, "crud/index.html", {"usuarios": usuarios})

def criar(request):
    nome = request.POST.get("nome")
    dataNascimento = request.POST.get("dataNascimento")
    email = request.POST.get("email")
    paisDestino = request.POST.get("paisDestino")
    Usuario.objects.create(nome=nome, dataNascimento=dataNascimento, email=email, paisDestino=paisDestino)
    usuarios = Usuario.objects.all()
    return render(request, "crud/index.html", {"usuarios": usuarios})

def editar(request, id):
    usuario = Usuario.objects.get(id=id)
    return render(request, "crud/editar.html", {"usuario": usuario})

def atualizar(request, id):
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
    return redirect(home)

def deletar(request, id):
    usuario = Usuario.objects.get(id=id)
    usuario.delete()
    return redirect(home)