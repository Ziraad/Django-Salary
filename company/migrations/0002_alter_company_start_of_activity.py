# Generated by Django 4.0.5 on 2023-07-13 11:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='start_of_activity',
            field=models.DateTimeField(default=datetime.date, verbose_name='تاریخ شروع فعالت'),
        ),
    ]
