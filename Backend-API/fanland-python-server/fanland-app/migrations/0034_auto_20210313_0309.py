# Generated by Django 3.1.7 on 2021-03-12 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0033_auto_20210313_0307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_detail',
            name='user_name',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]