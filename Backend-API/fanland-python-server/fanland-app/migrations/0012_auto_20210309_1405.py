# Generated by Django 3.1.7 on 2021-03-09 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0011_user_detail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_detail',
            name='admin_clubs',
            field=models.ManyToManyField(default=[], related_name='admin_clubs', to='todo.Fanclub'),
        ),
        migrations.AlterField(
            model_name='user_detail',
            name='following_clubs',
            field=models.ManyToManyField(default=[], related_name='following_clubs', to='todo.Fanclub'),
        ),
        migrations.AlterField(
            model_name='user_detail',
            name='liked_clubs',
            field=models.ManyToManyField(default=[], related_name='liked_clubs', to='todo.Fanclub'),
        ),
    ]
