# Generated by Django 3.2.7 on 2021-10-12 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_resource_resource'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='resource',
            field=models.FileField(upload_to='resources'),
        ),
    ]
