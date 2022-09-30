from django import forms
from .models import Project
from accounts.models import Profile

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title','description','in_scope','out_scope','team_size','duration']

class EOIForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['choice1','choice2','choice3']
