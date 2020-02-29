from django.contrib import admin
from .models import *
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
	list_display = ('description', 'end_date', 'status')

@admin.register(TodoList)
class TodoListAdmin(admin.ModelAdmin):
	list_display = ('title',)
	search_fields = ('title',)