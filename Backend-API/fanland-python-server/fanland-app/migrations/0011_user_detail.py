# Generated by Django 3.1.7 on 2021-03-09 08:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0010_auto_20210309_1338'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_clubs', models.ManyToManyField(related_name='admin_clubs', to='todo.Fanclub')),
                ('following_clubs', models.ManyToManyField(related_name='following_clubs', to='todo.Fanclub')),
                ('liked_clubs', models.ManyToManyField(related_name='liked_clubs', to='todo.Fanclub')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.user')),
            ],
        ),
    ]
