from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'galeria/index.html')

def imagem(request):
    return render(request, 'galeria/imagem.html')