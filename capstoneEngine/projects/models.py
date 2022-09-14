from django.db import models
from accounts.models import Profile

# Create your models here.

class Project(models.Model):
	sponsor_id = models.ForeignKey(Profile, on_delete = models.CASCADE)
	is_allocated = models.BooleanField(default = False)
	title = models.TextField(max_length = 500, blank = False)
	description = models.TextField(blank = False)
	in_scope = models.TextField(blank = False)
	out_scope = models.TextField(blank = False)
	skill = models.TextField(blank = False)
	team_size = models.IntegerField(blank = False)
	duration = models.IntegerField(blank=False)

