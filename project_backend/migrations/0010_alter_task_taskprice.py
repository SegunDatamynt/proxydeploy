# Generated by Django 4.1.5 on 2023-01-13 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_backend', '0009_alter_task_taskassignedby'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='taskPrice',
            field=models.DecimalField(decimal_places=2, max_digits=10, max_length=255),
        ),
    ]
