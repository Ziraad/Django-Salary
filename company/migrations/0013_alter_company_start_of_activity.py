# Generated by Django 4.0.5 on 2023-08-10 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0012_alter_company_start_of_activity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='start_of_activity',
            field=models.DateField(verbose_name='تاریخ شروع فعالت'),
        ),
    ]
