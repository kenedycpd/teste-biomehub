from django.forms import ModelForm
from .models import *

class TitleForm(ModelForm):
	class Meta:
		model = TodoList
		fields = '__all__'

class TaskForm(ModelForm):
	class Meta:
		model = Task
		fields = '__all__'