# Generated by Django 3.1.7 on 2021-03-05 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20210304_1805'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='userProfilePic',
            field=models.ImageField(default='', upload_to='media'),
        ),
    ]
