from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    class Identity(models.IntegerChoices):
        CONVENER = 1
        SPONSOR = 2
        STUDENT = 3
    class Units(models.IntegerChoices):
        DEFAULT = 0,'0'
        A = 9785,'9785'
        B = 9786, '9786'
        C = 10004, '10004'
        D = 10005, '10005'
        E = 10098, '10098'
        F = 11522, '11522'
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.TextField(max_length=500, blank=True)
    identity = models.IntegerField(choices=Identity.choices, default = 3)
    is_in_group = models.BooleanField(blank=True, default= False)
    unit_code = models.IntegerField(choices=Units.choices, blank=True)
    project_id = models.IntegerField(blank=True, null=True)
    choice1 = models.IntegerField(blank=True, null=True)
    choice2 = models.IntegerField(blank=True, null=True)
    choice3 = models.IntegerField(blank=True, null=True)
    



@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
