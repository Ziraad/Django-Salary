# Generated by Django 4.0.5 on 2022-08-27 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salary', '0008_decree_delete_warrant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='decree',
            name='type_of_employment',
            field=models.CharField(choices=[('Oficial', 'رسمی'), ('Contractual', 'قراردادی')], default='Contractual', max_length=20, verbose_name='نوع استخدام'),
        ),
    ]