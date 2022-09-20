from django.db import models
from accounts.models import Profile
from django.forms import ModelForm 

# Create your models here.

class Project(models.Model):
	sponsor_id = models.ForeignKey(Profile, on_delete = models.CASCADE)
	is_allocated = models.BooleanField(default = False)
	title = models.TextField(max_length = 500, default=' ' , blank = False)
	description = models.TextField(blank = False, default=' ')
	in_scope = models.TextField(blank = False, default=' ')
	out_scope = models.TextField(blank = False, default=' ')
	skill = models.TextField(blank = False, default=' ')
	team_size = models.IntegerField(blank = False, default=4)
	duration = models.IntegerField(blank=False,default=12)

