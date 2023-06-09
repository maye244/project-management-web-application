# Generated by Django 3.2.7 on 2021-10-02 08:07

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('end_date', models.DateTimeField(default=datetime.datetime.now)),
                ('project_code', models.CharField(max_length=20)),
                ('details', models.CharField(max_length=200)),
                ('team', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='to_do',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('start_date', models.DateTimeField(default=datetime.datetime.now)),
                ('due_date', models.DateTimeField(default=datetime.datetime.now)),
                ('project_code', models.CharField(max_length=20)),
                ('details', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='in_progress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('due_date', models.DateTimeField(default=datetime.datetime.now)),
                ('project_code', models.CharField(max_length=20)),
                ('details', models.CharField(max_length=200)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.to_do')),
            ],
        ),
        migrations.CreateModel(
            name='done',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('due_date', models.DateTimeField(default=datetime.datetime.now)),
                ('project_code', models.CharField(max_length=20)),
                ('details', models.CharField(max_length=200)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='user.to_do')),
            ],
        ),
    ]
