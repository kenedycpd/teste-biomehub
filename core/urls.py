from django.urls import include, path
from . import views
urlpatterns = [
path('adcionar/', views.adcionar, name='adcionar'),
path('titulo/', views.titulo, name='titulo'),
]