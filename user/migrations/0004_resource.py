# Generated by Django 3.2.7 on 2021-10-11 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20211008_0111'),
    ]

    operations = [
        migrations.CreateModel(
            name='resource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resource', models.FileField(upload_to='wikis')),
            ],
        ),
    ]
