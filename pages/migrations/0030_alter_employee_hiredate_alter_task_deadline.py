# Generated by Django 4.2.10 on 2024-03-17 20:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0029_alter_activity_donedate_alter_employee_hiredate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='HireDate',
            field=models.DateField(default=datetime.datetime(2024, 3, 17, 20, 58, 28, 447815)),
        ),
        migrations.AlterField(
            model_name='task',
            name='Deadline',
            field=models.DateField(default=datetime.datetime(2024, 3, 17, 20, 58, 28, 449069), null=True),
        ),
    ]
