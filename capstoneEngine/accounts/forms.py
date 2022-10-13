from django import forms
from .models import Profile
from django.utils.translation import gettext as _
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'identity', 'unit_code']
        widgets = {
            'name': forms.Textarea(attrs={'class': 'eleForI Huans'}),
            'identity': forms.Select(attrs={'class': 'eleForI Huans'}),
            'unit_code': forms.Select(attrs={'class': 'eleForI Huans'}),
        }

class UserForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'eleForI Huans'}))
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'eleForI Huans'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'class': 'eleForI Huans'})
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.Textarea(attrs={'class': 'eleForI Huans'}),
        }
