from django.shortcuts import render
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

def atualizar(request):
    usuarios = Usuario.objects.get(id=id)
    return render(request, "crud/atualizar.html", {"usuarios": usuarios})