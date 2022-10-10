from django.contrib import admin


# Register your models here.
from .models import Profile, Group

admin.site.register(Profile)
admin.site.register(Group)
