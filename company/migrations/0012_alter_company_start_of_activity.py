# Generated by Django 4.0.5 on 2023-08-10 11:37

from django.db import migrations
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0011_alter_company_start_of_activity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='start_of_activity',
            field=django_jalali.db.models.jDateField(verbose_name='تاریخ شروع فعالت'),
        ),
    ]
