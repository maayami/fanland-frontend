# Generated by Django 3.1.7 on 2021-03-09 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0025_auto_20210309_1922'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='message_type',
        ),
        migrations.AddField(
            model_name='chat',
            name='is_image_message',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
