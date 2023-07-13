import datetime
import time

from django.db import models
from django.conf import settings
from django.urls import reverse


class Company(models.Model):
    COMPANY_TYPE = (
        ('Private', 'خصوصی'),
        ('Government', 'دولتی'),
    )

    name = models.CharField('نام', max_length=200)
    slug = models.SlugField('اسلاگ', max_length=200, allow_unicode=True, unique=True)
    company_type = models.CharField(
        'نوع شرکت', max_length=20, choices=COMPANY_TYPE, default='Private')
    object = models.CharField('موضوع فعالیت', max_length=200)
    accountant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='حسابدار')
    address = models.CharField('آدرس', max_length=150, null=True, blank=True)
    logo = models.ImageField('لوگو', upload_to='images/logos/', default='images/logo.jpg')
    description = models.TextField('توضیحات', null=True, blank=True)
    start_of_activity = models.DateField('تاریخ شروع فعالت')
    is_active = models.BooleanField('فعال', default=False)
    created = models.DateTimeField('ایجاد شده در', auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("accounts:companies:company_detail", kwargs={"slug": self.slug})

    class Meta:
        ordering = ['created']
        verbose_name = 'شرکت'
        verbose_name_plural = 'شرکت'
