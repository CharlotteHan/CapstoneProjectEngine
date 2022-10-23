# Generated by Django 4.1 on 2022-10-23 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_alter_project_member'),
        ('accounts', '0018_alter_group_member'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='choice1',
            field=models.ForeignKey(blank=True, default='1', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='choice1', to='projects.project'),
        ),
        migrations.AlterField(
            model_name='group',
            name='choice2',
            field=models.ForeignKey(blank=True, default='1', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='choice2', to='projects.project'),
        ),
        migrations.AlterField(
            model_name='group',
            name='choice3',
            field=models.ForeignKey(blank=True, default='1', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='choice3', to='projects.project'),
        ),
        migrations.AlterField(
            model_name='group',
            name='is_allocated',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='group',
            name='member',
            field=models.ManyToManyField(blank=True, to='accounts.profile'),
        ),
    ]
