# Generated by Django 4.0.5 on 2023-07-13 11:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_alter_company_start_of_activity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='start_of_activity',
            field=models.DateField(default=datetime.date, verbose_name='تاریخ شروع فعالت'),
        ),
    ]