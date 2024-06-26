# Generated by Django 4.2.10 on 2024-03-15 15:00

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0027_alter_employee_hiredate_alter_task_deadline_activity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='DoneDate',
            field=models.DateTimeField(verbose_name=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='employee',
            name='HireDate',
            field=models.DateField(default=datetime.datetime(2024, 3, 15, 15, 0, 4, 951580)),
        ),
        migrations.AlterField(
            model_name='task',
            name='Deadline',
            field=models.DateField(default=datetime.datetime(2024, 3, 15, 15, 0, 4, 953005), null=True),
        ),
    ]
