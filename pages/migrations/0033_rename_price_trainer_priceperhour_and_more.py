# Generated by Django 4.2.10 on 2024-03-21 10:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0032_trainer_price_alter_employee_hiredate_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trainer',
            old_name='Price',
            new_name='PricePerHour',
        ),
        migrations.AddField(
            model_name='trainer',
            name='Certificate2',
            field=models.FileField(blank=True, null=True, upload_to='pdf'),
        ),
        migrations.AddField(
            model_name='trainer',
            name='Certificate3',
            field=models.FileField(blank=True, null=True, upload_to='pdf'),
        ),
        migrations.AddField(
            model_name='trainer',
            name='email',
            field=models.CharField(default='example@email.com', max_length=50),
        ),
        migrations.AlterField(
            model_name='employee',
            name='HireDate',
            field=models.DateField(default=datetime.datetime(2024, 3, 21, 10, 8, 30, 199186)),
        ),
        migrations.AlterField(
            model_name='task',
            name='Deadline',
            field=models.DateField(default=datetime.datetime(2024, 3, 21, 10, 8, 30, 200468), null=True),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='Certificates',
            field=models.FileField(blank=True, null=True, upload_to='pdf'),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='Qualifications',
            field=models.TextField(blank=True, null=True),
        ),
    ]
