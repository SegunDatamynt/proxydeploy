# Generated by Django 4.1.5 on 2023-01-12 17:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project_backend', '0005_tasks'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='tasks',
            table='Task',
        ),
    ]