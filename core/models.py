from django.db import models

class TodoList(models.Model):
	title = models.CharField('Titulo', max_length=50,blank=True)
	def __str__(self):
		return self.title

class Task(models.Model):

	status_choices = (
		('EX', 'Em execução'),
		('PD', 'Pendente'),
		('CD', 'Concluida')
		)

	
	description = models.TextField('Descrição', blank=True)
	end_date = models.DateField('Data Final', auto_now_add=False, blank=True, null=True)
	status = models.CharField('Status', max_length=2, choices=status_choices, blank=True)

	class Meta:
		verbose_name = 'Task'
		ordering = ['-description']
	def __str__(self):
		return self.description