# Generated by Django 4.0.5 on 2023-07-13 11:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('person', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=4, unique=True, verbose_name='سال')),
                ('base_salary', models.IntegerField(verbose_name='حقوق پایه')),
                ('base_years', models.IntegerField(default=0, verbose_name='پایه سنوات')),
                ('right_to_housing', models.IntegerField(blank=True, null=True, verbose_name='حق مسکن')),
                ('right_to_grocery', models.IntegerField(blank=True, null=True, verbose_name='حق خوار و بار')),
                ('right_to_children', models.IntegerField(blank=True, null=True, verbose_name='حق اولاد')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='ایجاد شده در')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='به روز رسانی در')),
            ],
            options={
                'verbose_name': 'اطلاعات پایه اداره کار',
                'verbose_name_plural': 'اطلاعات پایه اداره کار',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='TypeOfEmployment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='نام')),
                ('slug', models.SlugField(allow_unicode=True, max_length=70, verbose_name='اسلاگ')),
            ],
            options={
                'verbose_name': 'نوع استخدام',
                'verbose_name_plural': 'نوع استخدام',
            },
        ),
        migrations.CreateModel(
            name='TaxTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_wage', models.IntegerField(default=0, verbose_name='از درآمد')),
                ('to_wage', models.IntegerField(default=0, verbose_name='تا درآمد')),
                ('tax_percent', models.IntegerField(default=0, verbose_name='درصد مالیات')),
                ('base_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tax_table', to='salary.baseinfo', verbose_name='اطلاعات پایه')),
            ],
            options={
                'verbose_name': 'جدول مالیات',
                'verbose_name_plural': 'جدول مالیات',
            },
        ),
        migrations.CreateModel(
            name='SalaryReceipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month_name', models.CharField(choices=[('Farvardin', 'فروردین'), ('Ordibehesht', 'اردیبهشت'), ('Khordad', 'خرداد'), ('Tir', 'تیر'), ('Mordad', 'مرداد'), ('Shahrivar', 'شهریور'), ('Mehr', 'مهر'), ('Aban', 'آبان'), ('Azar', 'آذر'), ('Dey', 'دی'), ('Bahman', 'بهمن'), ('Esfand', 'اسفند')], max_length=20, verbose_name='ماه')),
                ('year', models.CharField(max_length=4, verbose_name='سال')),
                ('working_days', models.IntegerField(default=0, verbose_name='کارکرد')),
                ('overtime', models.IntegerField(default=0, verbose_name='اضافه کاری')),
                ('closed_work', models.IntegerField(default=0, verbose_name='تعطیل کاری')),
                ('mission', models.IntegerField(default=0, verbose_name='مأموریت')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='ایجاد شده در')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='به روز رسانی در')),
                ('monthly_wage', models.IntegerField(default=0, verbose_name='حقوق ماهیانه')),
                ('overtime_wage', models.IntegerField(default=0, verbose_name='اضافه کاری')),
                ('closed_work_wage', models.IntegerField(default=0, verbose_name='مبلغ تعطیل کاری')),
                ('mission_wage', models.IntegerField(default=0, verbose_name='مأموریت')),
                ('right_of_house', models.IntegerField(default=0, verbose_name='حق مسکن')),
                ('right_of_grocery', models.IntegerField(default=0, verbose_name='حق خوار و بار')),
                ('right_of_children', models.IntegerField(default=0, verbose_name='حق اولاد')),
                ('sub_total_wage', models.IntegerField(default=0, verbose_name='جمع حقوق و مزایا')),
                ('insurance', models.IntegerField(default=0, verbose_name='حق بیمه')),
                ('tax', models.IntegerField(default=0, verbose_name='مالیات')),
                ('loan_received', models.IntegerField(default=0, verbose_name='وام دریافتی')),
                ('other_deductions', models.IntegerField(default=0, verbose_name='سایر کسورات')),
                ('sub_total_deductions', models.IntegerField(default=0, verbose_name='جمع کسورات')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wage_creator', to=settings.AUTH_USER_MODEL, verbose_name='تهیه کننده')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wage_person', to='person.person', verbose_name='شخص')),
            ],
            options={
                'verbose_name': 'حقوق دریافتی',
                'verbose_name_plural': 'حقوق دریافتی',
            },
        ),
        migrations.CreateModel(
            name='Decree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=4, verbose_name='سال')),
                ('type_of_rule', models.CharField(choices=[('Private', 'خصوصی'), ('Government', 'دولتی'), ('Retireds', 'بازنشستگان')], default='Private', max_length=20, verbose_name='نوع حکم')),
                ('type_of_employment', models.CharField(choices=[('Oficial', 'رسمی'), ('Contractual', 'قراردادی')], default='Contractual', max_length=20, verbose_name='نوع استخدام')),
                ('base_salary', models.IntegerField(blank=True, default=0, null=True, verbose_name='حقوق پایه')),
                ('base_years', models.IntegerField(blank=True, default=0, null=True, verbose_name='سنوات')),
                ('reward', models.IntegerField(blank=True, default=0, null=True, verbose_name='پاداش')),
                ('right_to_housing', models.IntegerField(blank=True, default=0, null=True, verbose_name='حق مسکن')),
                ('right_to_grocery', models.IntegerField(blank=True, default=0, null=True, verbose_name='حق خوار و بار')),
                ('right_to_supervisor', models.IntegerField(blank=True, default=0, null=True, verbose_name='حق سرپرستی')),
                ('right_of_children', models.IntegerField(blank=True, default=0, null=True, verbose_name='حق اولاد')),
                ('service_location', models.CharField(blank=True, max_length=50, null=True, verbose_name='محل خدمت')),
                ('job_title', models.CharField(max_length=50, verbose_name='عنوان شغل')),
                ('organizational_unit', models.CharField(blank=True, max_length=50, null=True, verbose_name='واحد سازمانی')),
                ('organizational_position', models.CharField(blank=True, max_length=50, null=True, verbose_name='پست سازمانی')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='ایجاد شده در')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='به روز رسانی در')),
                ('company', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='decree_company', to='company.company', verbose_name='شرکت')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='decree_creator', to=settings.AUTH_USER_MODEL, verbose_name='تهیه کننده')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='decree_person', to='person.person', verbose_name='شخص')),
            ],
            options={
                'verbose_name': 'حکم حقوقی',
                'verbose_name_plural': 'حکم حقوقی',
                'ordering': ('-created',),
            },
        ),
    ]
