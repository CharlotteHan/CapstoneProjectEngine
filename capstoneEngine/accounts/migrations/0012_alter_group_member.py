# Generated by Django 4.1 on 2022-10-10 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_alter_group_choice1_alter_group_choice2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='member',
            field=models.ManyToManyField(blank=True, to='accounts.profile'),
        ),
    ]
