# Generated by Django 3.1.7 on 2021-03-19 06:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0043_auto_20210319_0059'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fan',
            name='last_active',
        ),
        migrations.AddField(
            model_name='fan',
            name='last_active_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fan',
            name='last_active_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
