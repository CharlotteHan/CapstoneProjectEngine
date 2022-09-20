from django import forms
from .models import Project



class ProjectForm(forms.ModelForm):
	class Meta:
		model = Project
		fields = ['title','description','in_scope','out_scope','team_size','duration']
