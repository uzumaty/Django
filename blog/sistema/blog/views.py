from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def base(request):
    return render(request, "base.html")

def publicaciones(request):
    return render(request, "publicaciones.html")

def otros(request):
    return render(request, "otros.html")

def inicio(request):
    return render(request, "inicio.html")

def muro(request):
    return render(request, "muro.html")