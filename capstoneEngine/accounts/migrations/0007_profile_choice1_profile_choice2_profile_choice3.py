# Generated by Django 4.1 on 2022-09-22 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_profile_project_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='choice1',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='choice2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='choice3',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]