from django.http import HttpResponse
from django.shortcuts import render

def mi_vista(request):
    return render(request, 'index.html')

def RegistroView(request):
    return render(request, 'registrarse.html')