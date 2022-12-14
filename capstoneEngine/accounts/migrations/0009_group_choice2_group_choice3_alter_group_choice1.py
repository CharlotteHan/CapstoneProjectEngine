# Generated by Django 4.1 on 2022-10-10 01:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
        ('accounts', '0008_alter_profile_unit_code_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='choice2',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='choice2', to='projects.project'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='group',
            name='choice3',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='choice3', to='projects.project'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='group',
            name='choice1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choice1', to='projects.project'),
        ),
    ]
