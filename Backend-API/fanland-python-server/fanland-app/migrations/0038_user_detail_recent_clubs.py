# Generated by Django 3.1.7 on 2021-03-14 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0037_auto_20210313_1648'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_detail',
            name='recent_clubs',
            field=models.ManyToManyField(blank=True, related_name='recent_clubs', to='todo.Fanclub'),
        ),
    ]
