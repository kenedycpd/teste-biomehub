from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required

def add_user(request):
	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			u = form.save()
			u.set_password(u.password)
			u.save()
			return redirect('user_login')
	else:
		form = UserForm()
	return render(request, 'accounts/add_user.html',{'form':form})

def user_login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user:
			login(request,user)
			return redirect('home')
		else:
			messages.error(request,'usuário ou senha invalidos')
	return render(request, 'accounts/login.html')

def logout_user(request):
	logout(request)
	return redirect('user_login')



def user_change_password(request):
	if request.method == 'POST':
		form = PasswordChangeForm(user=request.user, data=request.POST)
		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			messages.error(request, 'senha alterada com sucesso!')
			return redirect('user_login')
		else:
			messages.error(request, 'não foi possivel alterar sua senha!')
	else:
		form = PasswordChangeForm(user=request.user)
	return render(request, 'accounts/user_change_password.html',{'form':form})
