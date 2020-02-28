from django.shortcuts import render, redirect
from .models import *
from .forms import *

def home(request):
	return render(request, 'index.html')


def adcionar(request):
	if request.method == 'POST':
		form = TaskForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form = TaskForm()
	return render(request, 'core/formtask.html',{'form':form})

def titulo(request):
	if request.method == 'POST':
		form = TitleForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form = TitleForm()
	return render(request, 'core/titulo.html',{'form':form})