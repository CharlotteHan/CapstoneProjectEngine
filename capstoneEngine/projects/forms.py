from django import forms
from .models import Project
from accounts.models import Profile, Group
from django.utils.translation import gettext as _

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title','description','in_scope','out_scope','team_size','duration']

class EOIForm(forms.ModelForm):
    group_member1 = forms.CharField(max_length=50, label='Group Member ID', widget=forms.Textarea(attrs={'class': 'eleForI Huans'}))
    group_member2 = forms.CharField(max_length=50, label='Group Member ID', widget=forms.Textarea(attrs={'class': 'eleForI Huans'}))
    group_member3 = forms.CharField(max_length=50, label='Group Member ID', widget=forms.Textarea(attrs={'class': 'eleForI Huans'}), required=False)
    class Meta:
        model = Group
        fields = ['choice1','choice2','choice3']
        labels = {
            'choice1': _('Choice1'),
            'choice2': _('Choice2'),
            'choice3': _('Choice3'),
        }
        widgets = {
            'choice1': forms.Select(attrs={'class': 'eleForI Huans'}),
            'choice2': forms.Select(attrs={'class': 'eleForI Huans'}),
            'choice3': forms.Select(attrs={'class': 'eleForI Huans'}),
        }
        
class AllocateForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['member']
