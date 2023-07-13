# Generated by Django 4.0.5 on 2023-07-13 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('personnel_code', models.CharField(max_length=10, unique=True, verbose_name='کد پرسنلی')),
                ('first_name', models.CharField(max_length=50, verbose_name='نام')),
                ('last_name', models.CharField(max_length=50, verbose_name='نام خانوادگی')),
                ('nation_code', models.CharField(max_length=10, verbose_name='کد ملی')),
                ('image', models.ImageField(default='images/profile.png', upload_to='images/persons/', verbose_name='عکس')),
                ('date_of_birth', models.DateTimeField(blank=True, null=True, verbose_name='تاریخ تولد')),
                ('place_of_birth', models.CharField(blank=True, max_length=50, null=True, verbose_name='محل تولد')),
                ('father_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='نام پدر')),
                ('education_degree', models.CharField(blank=True, max_length=50, null=True, verbose_name='مدرک تحصیلی')),
                ('number_of_children', models.IntegerField(default=0, verbose_name='تعداد فرزندان')),
                ('marital_status', models.CharField(choices=[('Single', 'مجرد'), ('Married', 'متأهل')], max_length=20, verbose_name='وضعیت تأهل')),
                ('account_number', models.CharField(blank=True, max_length=20, null=True, verbose_name='شماره حساب بانکی')),
                ('is_active', models.BooleanField(default=False, verbose_name='فعال')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='ایجاد شده در')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='person_company', to='company.company', verbose_name='شرکت')),
            ],
            options={
                'verbose_name': 'شخص',
                'verbose_name_plural': 'شخص',
            },
        ),
    ]
