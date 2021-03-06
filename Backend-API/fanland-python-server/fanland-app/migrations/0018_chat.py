# Generated by Django 3.1.7 on 2021-03-09 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0017_auto_20210309_1506'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_image', models.CharField(max_length=200)),
                ('author_name', models.CharField(max_length=30)),
                ('message_type', models.IntegerField(default=0)),
                ('message', models.TextField()),
                ('date', models.DateTimeField()),
                ('chatroom_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.fanclub')),
            ],
        ),
    ]
