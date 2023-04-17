# Generated by Django 3.2.7 on 2021-10-19 12:30

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('due_date', models.DateTimeField(default=datetime.datetime.now)),
                ('project_code', models.CharField(max_length=20)),
                ('details', models.TextField()),
                ('member', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='resource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resource', models.FileField(upload_to='resources')),
            ],
        ),
        migrations.CreateModel(
            name='wiki',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='wikis')),
            ],
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('to_do', 'to_do'), ('in_progress', 'in_progress'), ('done', 'done')], default='to_do', max_length=20)),
                ('text', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('start_date', models.DateTimeField(default=datetime.datetime.now)),
                ('due_date', models.DateTimeField(default=datetime.datetime.now)),
                ('project_code', models.CharField(max_length=20)),
                ('details', models.TextField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo_lists.project')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employeeID', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=20)),
                ('projects', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo_lists.project')),
            ],
        ),
        migrations.CreateModel(
            name='Progress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=20)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('start_date', models.DateTimeField(default=datetime.datetime.now)),
                ('due_date', models.DateTimeField(default=datetime.datetime.now)),
                ('project_code', models.CharField(max_length=20)),
                ('details', models.TextField()),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo_lists.todo')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo_lists.project')),
            ],
        ),
        migrations.CreateModel(
            name='Done',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=20)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('start_date', models.DateTimeField(default=datetime.datetime.now)),
                ('due_date', models.DateTimeField(default=datetime.datetime.now)),
                ('project_code', models.CharField(max_length=20)),
                ('details', models.TextField()),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo_lists.todo')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo_lists.project')),
            ],
        ),
    ]
