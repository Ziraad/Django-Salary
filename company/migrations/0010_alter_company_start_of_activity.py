# Generated by Django 4.0.5 on 2023-08-10 10:03

import datetime
from django.db import migrations
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0009_alter_company_start_of_activity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='start_of_activity',
            field=django_jalali.db.models.jDateField(default=datetime.date(2023, 8, 10), verbose_name='تاریخ شروع فعالت'),
        ),
    ]