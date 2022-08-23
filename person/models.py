from django.db import models

from company.models import Company


class Person(models.Model):
    class Meta:
        verbose_name = "شخص"
        verbose_name_plural = "شخص"

    MARITAL_STATUS = (
        ('Single', 'مجرد'),
        ('Married', 'متأهل')
    )
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name='person_company', null=True, verbose_name='شرکت')
    personnel_code = models.CharField('کد پرسنلی', max_length=10, unique=True)
    first_name = models.CharField('نام', max_length=50)
    last_name = models.CharField('نام خانوادگی', max_length=50)
    nation_code = models.CharField('کد ملی', max_length=10)
    # id_code = models.CharField('کد', max_length=10)
    image = models.ImageField('عکس', upload_to='images/persons/', default='images/profile.png')
    date_of_birth = models.DateTimeField('تاریخ تولد', null=True, blank=True)
    place_of_birth = models.CharField('محل تولد', max_length=50, null=True, blank=True)
    father_name = models.CharField('نام پدر', max_length=50, null=True, blank=True)
    education_degree = models.CharField('مدرک تحصیلی', max_length=50, null=True, blank=True)
    number_of_children = models.IntegerField('تعداد فرزندان', default=0)
    marital_status = models.CharField(
        'وضعیت تأهل', max_length=20, choices=MARITAL_STATUS)
    is_active = models.BooleanField('فعال', default=False)
    created = models.DateTimeField('ایجاد شده در', auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def full_name(self):
        return self.last_name + ' ' + self.first_name

    def __str__(self):
        return '{} - {} {}'.format(self.personnel_code, self.first_name, self.last_name)
