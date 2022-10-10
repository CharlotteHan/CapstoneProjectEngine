from django import forms
from .models import Project
from accounts.models import Profile, Group
from django.utils.translation import gettext as _

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title','description','in_scope','out_scope','team_size','duration']

class EOIForm(forms.ModelForm):
    group_member1 = forms.CharField(max_length=50, label='Group Member ID')
    group_member2 = forms.CharField(max_length=50, label='Group Member ID')
    group_member3 = forms.CharField(max_length=50, label='Group Member ID', required=False)
    class Meta:
        model = Group
        fields = ['choice1','choice2','choice3']
        labels = {
            'choice1': _('Choice1'),
            'choice2': _('Choice2'),
            'choice3': _('Choice3'),
        }
