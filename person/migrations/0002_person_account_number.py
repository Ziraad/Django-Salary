# Generated by Django 4.0.5 on 2023-07-08 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='account_number',
            field=models.CharField(max_length=20, null=True, verbose_name='شماره حساب بانکی'),
        ),
    ]
