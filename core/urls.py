from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('calculadora-imc/', views.calculadora_imc, name='calculadora_imc'),
]
