# Generated by Django 3.1.7 on 2021-03-09 08:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0013_auto_20210309_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fanclub',
            name='admin_members',
            field=models.ManyToManyField(blank=True, default=[models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creator', to='todo.user')], related_name='admin_members', to='todo.User'),
        ),
        migrations.AlterField(
            model_name='fanclub',
            name='members',
            field=models.ManyToManyField(blank=True, default=[models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creator', to='todo.user')], related_name='members', to='todo.User'),
        ),
        migrations.AlterField(
            model_name='fanclub',
            name='top_fans',
            field=models.ManyToManyField(blank=True, default=[models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creator', to='todo.user')], related_name='top_fans', to='todo.User'),
        ),
    ]