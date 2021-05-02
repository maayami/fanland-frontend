# Generated by Django 3.1.7 on 2021-03-09 08:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0009_auto_20210309_1227'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='admin_clubs',
        ),
        migrations.RemoveField(
            model_name='user',
            name='following_clubs',
        ),
        migrations.RemoveField(
            model_name='user',
            name='liked_clubs',
        ),
        migrations.AddField(
            model_name='fanclub',
            name='admin_members',
            field=models.ManyToManyField(related_name='admin_members', to='todo.User'),
        ),
        migrations.AddField(
            model_name='fanclub',
            name='banned_users',
            field=models.ManyToManyField(related_name='banned_user', to='todo.User'),
        ),
        migrations.AddField(
            model_name='fanclub',
            name='creator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='creator', to='todo.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fanclub',
            name='members',
            field=models.ManyToManyField(related_name='members', to='todo.User'),
        ),
        migrations.AddField(
            model_name='fanclub',
            name='top_fans',
            field=models.ManyToManyField(related_name='top_fans', to='todo.User'),
        ),
    ]
