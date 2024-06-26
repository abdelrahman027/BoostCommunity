# Generated by Django 4.2.10 on 2024-03-19 13:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0030_alter_employee_hiredate_alter_task_deadline'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainer',
            name='Location',
            field=models.TextField(default='EGY'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='HireDate',
            field=models.DateField(default=datetime.datetime(2024, 3, 19, 13, 5, 40, 336442)),
        ),
        migrations.AlterField(
            model_name='task',
            name='Deadline',
            field=models.DateField(default=datetime.datetime(2024, 3, 19, 13, 5, 40, 337931), null=True),
        ),
    ]
