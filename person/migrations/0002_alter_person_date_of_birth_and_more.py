# Generated by Django 4.0.5 on 2023-08-10 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True, verbose_name='تاریخ تولد'),
        ),
        migrations.AlterField(
            model_name='person',
            name='personnel_code',
            field=models.CharField(max_length=10, verbose_name='کد پرسنلی'),
        ),
    ]