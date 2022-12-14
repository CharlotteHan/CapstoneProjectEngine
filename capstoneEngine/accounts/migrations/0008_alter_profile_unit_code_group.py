# Generated by Django 4.1 on 2022-10-10 00:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
        ('accounts', '0007_profile_choice1_profile_choice2_profile_choice3'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='unit_code',
            field=models.IntegerField(blank=True, choices=[(0, '0'), (9785, '9785'), (9786, '9786'), (10004, '10004'), (10005, '10005'), (10098, '10098'), (11522, '11522')]),
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
                ('member', models.ManyToManyField(to='accounts.profile')),
            ],
        ),
    ]
