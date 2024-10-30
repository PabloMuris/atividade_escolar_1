from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def calculadora_imc(request):
    return render(request, 'calculadora_imc.html')

