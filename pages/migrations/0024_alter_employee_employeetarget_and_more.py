# Generated by Django 4.2.10 on 2024-02-28 13:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0023_employee_employeetarget_alter_employee_hiredate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='EmployeeTarget',
            field=models.IntegerField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='HireDate',
            field=models.DateField(default=datetime.datetime(2024, 2, 28, 13, 58, 14, 840613)),
        ),
        migrations.AlterField(
            model_name='task',
            name='Deadline',
            field=models.DateField(default=datetime.datetime(2024, 2, 28, 13, 58, 14, 841711), null=True),
        ),
    ]
