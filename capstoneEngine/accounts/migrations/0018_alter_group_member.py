# Generated by Django 4.1 on 2022-10-23 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_alter_profile_unit_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='member',
            field=models.ManyToManyField(blank=True, null=True, to='accounts.profile'),
        ),
    ]
