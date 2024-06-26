# Generated by Django 4.2.10 on 2024-03-15 14:55

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0026_employee_mintarget_alter_employee_hiredate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='HireDate',
            field=models.DateField(default=datetime.datetime(2024, 3, 15, 14, 55, 5, 923821)),
        ),
        migrations.AlterField(
            model_name='task',
            name='Deadline',
            field=models.DateField(default=datetime.datetime(2024, 3, 15, 14, 55, 5, 925026), null=True),
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('ActivityID', models.AutoField(primary_key=True, serialize=False)),
                ('ActivityName', models.CharField(max_length=255)),
                ('Description', models.TextField(default='default description', null=True)),
                ('Project', models.CharField(blank=True, max_length=20, null=True)),
                ('DoneDate', models.DateField(verbose_name=django.utils.timezone.now)),
                ('Employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.employee')),
            ],
        ),
    ]
