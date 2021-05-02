# Generated by Django 3.1.7 on 2021-03-09 13:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0024_fanclub_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='time',
            field=models.TimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='chat',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='fanclub',
            name='image',
            field=models.ImageField(blank=True, default='fanclub_media/defaultfanclub.jpg', upload_to='fanclub_media'),
        ),
    ]
