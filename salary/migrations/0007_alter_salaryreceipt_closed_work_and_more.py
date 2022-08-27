# Generated by Django 4.0.5 on 2022-08-23 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salary', '0006_alter_salaryreceipt_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salaryreceipt',
            name='closed_work',
            field=models.IntegerField(default=0, verbose_name='تعطیل کاری'),
        ),
        migrations.AlterField(
            model_name='salaryreceipt',
            name='mission',
            field=models.IntegerField(default=0, verbose_name='مأموریت'),
        ),
        migrations.AlterField(
            model_name='salaryreceipt',
            name='overtime',
            field=models.IntegerField(default=0, verbose_name='اضافه کاری'),
        ),
        migrations.AlterField(
            model_name='salaryreceipt',
            name='working_days',
            field=models.IntegerField(default=0, verbose_name='کارکرد'),
        ),
    ]