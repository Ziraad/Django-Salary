# Generated by Django 4.0.5 on 2023-06-16 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salary', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseinfo',
            name='base_years',
            field=models.IntegerField(blank=True, default=0, verbose_name='پایه سنوات'),
        ),
    ]
