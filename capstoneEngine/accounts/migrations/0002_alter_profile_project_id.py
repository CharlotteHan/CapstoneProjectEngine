# Generated by Django 4.1 on 2022-09-22 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='project_id',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
