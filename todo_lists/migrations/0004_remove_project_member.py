# Generated by Django 3.2.7 on 2021-10-26 08:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_lists', '0003_todo_priority_level'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='member',
        ),
    ]
