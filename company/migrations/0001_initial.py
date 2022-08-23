# Generated by Django 4.0.5 on 2022-08-23 11:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='نام')),
                ('slug', models.SlugField(allow_unicode=True, max_length=200, unique=True, verbose_name='اسلاگ')),
                ('company_type', models.CharField(choices=[('Private', 'خصوصی'), ('Government', 'دولتی')], default='Private', max_length=20, verbose_name='نوع شرکت')),
                ('object', models.CharField(max_length=200, verbose_name='موضوع فعالیت')),
                ('address', models.CharField(blank=True, max_length=150, null=True, verbose_name='آدرس')),
                ('logo', models.ImageField(default='images/logo.jpg', upload_to='images/logos/', verbose_name='لوگو')),
                ('description', models.TextField(blank=True, null=True, verbose_name='توضیحات')),
                ('is_active', models.BooleanField(default=False, verbose_name='فعال')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='ایجاد شده در')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('accountant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='حسابدار')),
            ],
            options={
                'verbose_name': 'شرکت',
                'verbose_name_plural': 'شرکت',
                'ordering': ['created'],
            },
        ),
    ]
