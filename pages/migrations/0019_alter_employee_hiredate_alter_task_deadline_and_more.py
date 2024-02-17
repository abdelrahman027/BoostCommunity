# Generated by Django 4.2.10 on 2024-02-16 21:28

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0018_task_status_alter_employee_hiredate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='HireDate',
            field=models.DateField(default=datetime.datetime(2024, 2, 16, 21, 28, 57, 215065)),
        ),
        migrations.AlterField(
            model_name='task',
            name='Deadline',
            field=models.DateField(default=datetime.datetime(2024, 2, 16, 21, 28, 57, 216209), null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='Status',
            field=models.ForeignKey(default='inprogress', null=True, on_delete=django.db.models.deletion.CASCADE, to='pages.status'),
        ),
    ]
