# Generated by Django 4.2.10 on 2024-02-28 18:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0025_alter_employee_hiredate_alter_task_deadline'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='MinTarget',
            field=models.IntegerField(blank=True, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='HireDate',
            field=models.DateField(default=datetime.datetime(2024, 2, 28, 18, 0, 53, 448657)),
        ),
        migrations.AlterField(
            model_name='task',
            name='Deadline',
            field=models.DateField(default=datetime.datetime(2024, 2, 28, 18, 0, 53, 449879), null=True),
        ),
    ]
