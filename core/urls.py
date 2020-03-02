from django.urls import include, path
from . import views
urlpatterns = [
path('adcionar/', views.adcionar, name='adcionar'),
path('lista_title/', views.lista_title, name='lista_title'),
path('editar_titulo/<int:id_adcionar>/', views.editar_titulo,name='editar_titulo'),
path('editar_tarefa/<int:id_adcionar>/', views.editar_tarefa,name='editar_tarefa'),
path('deletar_titulo/<int:id_adcionar>/', views.deletar_titulo,name='deletar_titulo'),
path('deletar_tarefa/<int:id_adcionar>/', views.deletar_tarefa,name='deletar_tarefa'),

]