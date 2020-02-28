from django.contrib import admin
from .models import *

@admin.register(TodoList)
class TodoListAdmin(admin.ModelAdmin):
	list_display = ('title',)
	search_fields = ('title',)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
	list_display = ('title', 'description', 'end_date', 'status')
	search_fields = ('title',)