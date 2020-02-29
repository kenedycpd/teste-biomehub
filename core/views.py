from django.shortcuts import render, redirect
from .models import *
from .forms import *

def home(request):
	return render(request, 'index.html')

def adcionar(request):
	if request.method == 'POST':
		form = TaskForm(request.POST)
		form2 = TitleForm(request.POST)
		if form.is_valid() and form2.is_valid():
			form.save()
			return redirect('home')
	else:
		form = TaskForm()
		form2 = TitleForm()
	return render(request, 'core/formtask.html',{'form':form,'form2':form2})

