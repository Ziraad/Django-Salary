# Generated by Django 4.0.5 on 2023-07-09 10:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('salary', '0004_salaryreceipt_insurance_salaryreceipt_loan_received_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaxTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_wage', models.IntegerField(default=0, verbose_name='از درآمد')),
                ('to_wage', models.IntegerField(default=0, verbose_name='تا درآمد')),
                ('tax_percent', models.IntegerField(default=0, verbose_name='درصد مالیات')),
                ('base_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salary.baseinfo', verbose_name='اطلاعات پایه')),
            ],
            options={
                'verbose_name': 'جدول مالیات',
                'verbose_name_plural': 'جدول مالیات',
            },
        ),
    ]
