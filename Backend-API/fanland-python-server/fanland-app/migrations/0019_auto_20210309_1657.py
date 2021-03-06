# Generated by Django 3.1.7 on 2021-03-09 11:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0018_chat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='chat',
            name='message',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='chat',
            name='message_type',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
