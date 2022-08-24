from calendar import month_name
from django.db import models
from person.models import Person
from django.conf import settings
from company.models import Company


class TypeOfEmployment(models.Model):
    class Meta:
        verbose_name = 'نوع استخدام'
        verbose_name_plural = 'نوع استخدام'

    name = models.CharField('نام', max_length=50)
    slug = models.SlugField('اسلاگ', max_length=70, allow_unicode=True)

    def __str__(self):
        return self.name


class BaseInfo(models.Model):
    class Meta:
        ordering = ('-created',)
        verbose_name = 'اطلاعات پایه اداره کار'
        verbose_name_plural = 'اطلاعات پایه اداره کار'

    year = models.CharField('سال', max_length=4, unique=True)
    base_salary = models.IntegerField('حقوق پایه')
    base_years = models.IntegerField('پایه سنوات', blank=True)
    right_to_housing = models.IntegerField('حق مسکن', null=True, blank=True)
    right_to_grocery = models.IntegerField('حق خوار و بار', null=True, blank=True)
    right_to_children = models.IntegerField('حق اولاد', null=True, blank=True)
    created = models.DateTimeField('ایجاد شده در', auto_now_add=True)
    updated = models.DateTimeField('به روز رسانی در', auto_now=True)


class Warrant (models.Model):
    class Meta:
        ordering = ('-created',)
        verbose_name = 'حکم حقوقی'
        verbose_name_plural = 'حکم حقوقی'

    TYPE_OF_RULE = (
        ('Private', 'خصوصی'),
        ('Government', 'دولتی'),
        ('Retireds', 'بازنشستگان'),
    )

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='rule_creator',
                                   verbose_name='تهیه کننده')
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name='rule_company', blank=True, verbose_name='شرکت')
    person = models.ForeignKey(
        Person, on_delete=models.CASCADE, related_name='rule_person', verbose_name='شخص')
    year = models.CharField('سال', max_length=4)
    type_of_rule = models.CharField('نوع حکم',
                                    max_length=20, choices=TYPE_OF_RULE, default='Private')
    type_of_employment = models.ForeignKey(
        TypeOfEmployment, on_delete=models.CASCADE, verbose_name='نوع استخدام')
    base_salary = models.IntegerField('حقوق پایه')
    base_years = models.IntegerField('سنوات', null=True, blank=True)
    reward = models.IntegerField('پاداش', null=True, blank=True)
    right_to_housing = models.IntegerField('حق مسکن', null=True, blank=True)
    right_to_grocery = models.IntegerField('حق خوار و بار', null=True, blank=True)
    right_to_supervisor = models.IntegerField('حق سرپرستی', null=True, blank=True)
    service_location = models.CharField('محل خدمت', max_length=50, null=True, blank=True)
    job_title = models.CharField('عنوان شغل', max_length=50)
    organizational_unit = models.CharField('واحد سازمانی', max_length=50, null=True, blank=True)
    organizational_position = models.CharField('پست سازمانی', max_length=50, null=True, blank=True)
    created = models.DateTimeField('ایجاد شده در', auto_now_add=True)
    updated = models.DateTimeField('به روز رسانی در', auto_now=True)

    def __str__(self):
        return '{} - {} - {}'.format(self.company.name, self.year, self.person.full_name)


class SalaryReceipt(models.Model):
    class Meta:
        verbose_name = 'حقوق دریافتی'
        verbose_name_plural = 'حقوق دریافتی'

    MONTH_NAME = (
        ('Farvardin', 'فروردین'),
        ('Ordibehesht', 'اردیبهشت'),
        ('Khordad', 'خرداد'),
        ('Tir', 'تیر'),
        ('Mordad', 'مرداد'),
        ('Shahrivar', 'شهریور'),
        ('Mehr', 'مهر'),
        ('Aban', 'آبان'),
        ('Azar', 'آذر'),
        ('Dey', 'دی'),
        ('Bahman', 'بهمن'),
        ('Esfand', 'اسفند'),
    )
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='wage_creator',
                                   verbose_name='تهیه کننده')
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='wage_person', verbose_name='شخص')
    month_name = models.CharField('ماه', max_length=20, choices=MONTH_NAME)
    year = models.CharField('سال', max_length=4)
    working_days = models.IntegerField('کارکرد', default=0)
    overtime = models.IntegerField('اضافه کاری', default=0)
    closed_work = models.IntegerField('تعطیل کاری', default=0)
    mission = models.IntegerField('مأموریت', default=0)
    created = models.DateTimeField('ایجاد شده در', auto_now_add=True)
    updated = models.DateTimeField('به روز رسانی در', auto_now=True)

    @staticmethod
    def calculate_free_salary(base_salary, working_days, overtime, closed_work, mission, reward, number_of_children):
        base_info = BaseInfo.objects.all().first()
        monthly_wage = int(float(working_days) * float(base_salary))
        overtime_wage = int(float(base_salary) / 7.33 * 1.4 * float(overtime))
        closed_work_wage = int(float(base_salary) * 1.4 * float(closed_work))
        mission_wage = int(float(base_salary) * 1.4 * float(mission))
        right_of_house = int(base_info.right_to_housing / 31 * float(working_days))  # fix bug 29 or 30 or 31 days
        right_of_grocery = int(base_info.right_to_grocery / 31 * float(working_days))  # fix bug 29 or 30 or 31 days
        right_of_children = int(base_info.right_to_children * float(number_of_children) * float(working_days))  # fix
        # bug 29 or 30 or 31 days

        sub_total_wage = int(monthly_wage) + int(overtime_wage) + int(closed_work_wage) + int(
            mission_wage) + int(right_of_house) + int(right_of_grocery) + int(right_of_children)

        return {
            'monthly_wage': monthly_wage,
            'overtime_wage': overtime_wage,
            'closed_work_wage': closed_work_wage,
            'mission_wage': mission_wage,
            'right_of_house': right_of_house,
            'right_of_grocery': right_of_grocery,
            'right_of_children': right_of_children,
            'sub_total_wage': sub_total_wage
        }

    def calculate_monthly_wage(self):
        warrant = Warrant.objects.get(person=self.person)
        daily_wage = warrant.base_salary
        monthly_wage = self.working_days * daily_wage

        return monthly_wage

    def calculate_overtime_wage(self):
        warrant = Warrant.objects.get(person=self.person)
        daily_wage = warrant.base_salary
        overtime_wage = daily_wage / 7.33 * 1.4 * self.overtime

        return overtime_wage

    def calculate_closed_work_wage(self):
        warrant = Warrant.objects.get(person=self.person)
        daily_wage = Warrant.base_salary
        closed_work = daily_wage * 1.4 * self.closed_work

        return closed_work

    def sub_salary_and_benefits(self):
        pass

    def sub_salary_and_benefits_covered_by_insurance(self):
        pass

    def calculate_insurance(self):
        return (self.sub_salary_and_benefits_covered_by_insurance * 7) / 100

    def calculate_tax(self):
        pass

    def collect_deductions(self):
        pass
