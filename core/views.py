from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
	return render(request, 'index.html')

@login_required
def adcionar(request):
	if request.method == 'POST':
		form = TaskForm(request.POST)
		form2 = TitleForm(request.POST)
		if form.is_valid() and form2.is_valid():
			form.save()
			form2.save()
			return redirect('lista_title')
	else:
		form = TaskForm()
		form2 = TitleForm()
	return render(request, 'core/formtask.html',{'form':form,'form2':form2})

@login_required
def editar_titulo(request, id_adcionar):
	edite = get_object_or_404(TodoList, id=id_adcionar)
	if request.method == 'POST':
		form2 = TitleForm(request.POST, instance=edite)
		if form2.is_valid():
			form2.save()
			return redirect('lista_title')
	else:
		form = TaskForm()
		form2 = TitleForm(instance=edite)
	return render(request, 'core/formtask.html',{'form':form, 'form2':form2})

@login_required
def editar_tarefa(request, id_adcionar):
	edite_2 = get_object_or_404(Task, id=id_adcionar)
	if request.method == 'POST':
		form = TaskForm(request.POST, instance=edite_2)
		if form.is_valid():
			form.save()
			return redirect('lista_title')
	else:
		form = TaskForm(instance=edite_2)
		form2 = TitleForm()
	return render(request, 'core/formtask.html',{'form':form, 'form2':form2})

@login_required
def deletar_titulo(request, id_adcionar):
	exclui_titulo = TodoList.objects.get(id=id_adcionar).delete()
	return redirect('lista_title')

@login_required
def deletar_tarefa(request, id_adcionar):
	exclui_tarefa = Task.objects.get(id=id_adcionar).delete()
	return redirect('lista_title')
	
@login_required
def lista_title(request):
	lista = TodoList.objects.all()
	lista_2 = Task.objects.all()
	return render(request, 'core/list.html',{'lista':lista, 'lista_2':lista_2})