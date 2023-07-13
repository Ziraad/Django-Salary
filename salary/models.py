from django.db import models
from django.shortcuts import get_object_or_404
from django.urls import reverse

from person.models import Person
from django.conf import settings
from company.models import Company
import uuid


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
    base_years = models.IntegerField('پایه سنوات', default=0)
    right_to_housing = models.IntegerField('حق مسکن', null=True, blank=True)
    right_to_grocery = models.IntegerField('حق خوار و بار', null=True, blank=True)
    right_to_children = models.IntegerField('حق اولاد', null=True, blank=True)
    created = models.DateTimeField('ایجاد شده در', auto_now_add=True)
    updated = models.DateTimeField('به روز رسانی در', auto_now=True)


class TaxTable(models.Model):
    class Meta:
        verbose_name = 'جدول مالیات'
        verbose_name_plural = 'جدول مالیات'

    base_info = models.ForeignKey(BaseInfo, on_delete=models.CASCADE, related_name='tax_table', verbose_name='اطلاعات پایه')
    from_wage = models.IntegerField('از درآمد', default=0)
    to_wage = models.IntegerField('تا درآمد', default=0)
    tax_percent = models.IntegerField('درصد مالیات', default=0)

    def __str__(self):
        return '{} - {} - {} - {}'.format(self.base_info, self.from_wage, self.to_wage, self.tax_percent)


class Decree(models.Model):
    class Meta:
        ordering = ('-created',)
        verbose_name = 'حکم حقوقی'
        verbose_name_plural = 'حکم حقوقی'

    TYPE_OF_RULE = (
        ('Private', 'خصوصی'),
        ('Government', 'دولتی'),
        ('Retireds', 'بازنشستگان'),
    )

    TYPE_OF_EMPLOYMENT = (
        ('Oficial', 'رسمی'),
        ('Contractual', 'قراردادی'),
    )

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='decree_creator',
                                   verbose_name='تهیه کننده')
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name='decree_company', blank=True, verbose_name='شرکت')
    person = models.ForeignKey(
        Person, on_delete=models.CASCADE, related_name='decree_person', verbose_name='شخص')
    year = models.CharField('سال', max_length=4)
    type_of_rule = models.CharField('نوع حکم',
                                    max_length=20, choices=TYPE_OF_RULE, default='Private')
    type_of_employment = models.CharField('نوع استخدام',
                                          max_length=20, choices=TYPE_OF_EMPLOYMENT, default='Contractual')
    base_salary = models.IntegerField('حقوق پایه', default=0, null=True, blank=True)
    base_years = models.IntegerField('سنوات', default=0, null=True, blank=True)
    reward = models.IntegerField('پاداش', default=0, null=True, blank=True)
    right_to_housing = models.IntegerField('حق مسکن', default=0, null=True, blank=True)
    right_to_grocery = models.IntegerField('حق خوار و بار', default=0, null=True, blank=True)
    right_to_supervisor = models.IntegerField('حق سرپرستی', default=0, null=True, blank=True)
    right_of_children = models.IntegerField('حق اولاد', default=0, null=True, blank=True)
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
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
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

    monthly_wage = models.IntegerField('حقوق ماهیانه', default=0)
    overtime_wage = models.IntegerField('اضافه کاری', default=0)
    closed_work_wage = models.IntegerField('مبلغ تعطیل کاری', default=0)
    mission_wage = models.IntegerField('مأموریت', default=0)
    right_of_house = models.IntegerField('حق مسکن', default=0)
    right_of_grocery = models.IntegerField('حق خوار و بار', default=0)
    right_of_children = models.IntegerField('حق اولاد', default=0)
    sub_total_wage = models.IntegerField('جمع حقوق و مزایا', default=0)

    insurance = models.IntegerField('حق بیمه', default=0)
    tax = models.IntegerField('مالیات', default=0)
    loan_received = models.IntegerField('وام دریافتی', default=0)
    other_deductions = models.IntegerField('سایر کسورات', default=0)
    sub_total_deductions = models.IntegerField('جمع کسورات', default=0)

    def __unicode__(self):
        return self.id

    def __str__(self):
        return self.person.personnel_code

    def get_absolute_url(self):
        return reverse("person:wage_detail", kwargs={"wage_id": self.id})

    @staticmethod
    def calculate_free_salary(year, base_salary, base_years, working_days, overtime, closed_work, mission, reward,
                              number_of_children, number_of_days):
        try:
            base_info = BaseInfo.objects.filter(year=year)
            print('base info: ', base_info)
            assert base_info.exists(), 'برای سال مورد نظر، حقوق و دستمزد تعریف نشده است'
            base_info = BaseInfo.objects.get(year=year)
            base_years_wage = int(float(base_years))
            print('base info is get: ', base_info)
            monthly_wage = int(float(working_days) * float(base_salary))
            overtime_wage = int(float(base_salary) / 7.33 * 1.4 * float(overtime))
            closed_work_wage = int(float(base_salary) * 1.4 * float(closed_work))
            mission_wage = int(float(base_salary) * 1.4 * float(mission))
            right_of_house = int(base_info.right_to_housing / number_of_days * float(working_days))
            right_of_grocery = int(base_info.right_to_grocery / number_of_days * float(working_days))
            right_of_children = int(
                (base_info.right_to_children / number_of_days) * float(working_days) * float(number_of_children))

            sub_total_wage = int(monthly_wage) + int(base_years_wage) + int(overtime_wage) + int(
                closed_work_wage) + int(
                mission_wage) + int(right_of_house) + int(right_of_grocery) + int(right_of_children)
            print('sub total wage: ', sub_total_wage)
            print('before return in def')

            return {
                'monthly_wage': monthly_wage,
                'base_years_wage': base_years_wage,
                'overtime_wage': overtime_wage,
                'closed_work_wage': closed_work_wage,
                'mission_wage': mission_wage,
                'right_of_house': right_of_house,
                'right_of_grocery': right_of_grocery,
                'right_of_children': right_of_children,
                'sub_total_wage': sub_total_wage
            }
        except Exception as e:
            raise Exception(e)

    def calculate_salary(self, month_name, year, working_days, overtime, closed_work, mission):
        print('***********************************************************')
        print('in def calculate salary')
        print('month_name: ', month_name)
        print('year: ', year)
        print('working_days: ', working_days)
        print('overtime: ', overtime)
        print('closed_work: ', closed_work)
        print('mission: ', mission)
        print('***********************************************************')
        try:
            print('***********************************************************')
            print('in try definition')
            person = self.person
            print('person: ', person)
            decree = get_object_or_404(Decree, person=person, year=year)
            right_to_housing = decree.right_to_housing
            right_to_grocery = decree.right_to_grocery
            print('decree: ', decree)
            number_of_children = decree.person.number_of_children
            right_of_children = decree.right_of_children
            print('number_of_children: ', number_of_children)
            base_salary = decree.base_salary
            print('base_salary: ', base_salary)
            print('***********************************************************')
            self.monthly_wage = int(working_days) * int(base_salary)
            print('monthly_wage: ', self.monthly_wage)
            self.overtime_wage = int(float(base_salary) / 7.33 * 1.4 * float(overtime))
            print('overtime_wage: ', self.overtime_wage)
            self.closed_work_wage = int(float(base_salary) * 1.4 * float(closed_work))
            print('closed_work_wage: ', self.closed_work_wage)
            self.mission_wage = int(float(base_salary) * 1.4 * float(mission))
            print('mission_wage: ', self.mission_wage)
            self.right_of_house = int(right_to_housing / 31 * float(working_days))  # fix bug 29 or 30 or 31 days
            print('right_of_house: ', self.right_of_house)
            self.right_of_grocery = int(right_to_grocery / 31 * float(working_days))  # fix bug 29 or 30 or 31 days
            print('right_of_grocery: ', self.right_of_grocery)
            self.right_of_children = int(number_of_children) * (int(right_of_children) / 31) * int(working_days)
            print('right_of_children: ', self.right_of_children)

            self.sub_total_wage = int(self.monthly_wage) + int(self.overtime_wage) + int(self.closed_work_wage) + int(
                self.mission_wage) + int(self.right_of_house) + int(self.right_of_grocery) + int(self.right_of_children)

            base_info = BaseInfo.objects.filter(year=year)
            assert base_info.exists(), 'برای سال مورد نظر جدول حقوق و دستمزد یافت نشد. لطفاً با پشتیبانی تماس بگیرید.'
            base_info = get_object_or_404(BaseInfo, year=year)
            self.calculate_insurance()
            self.calculate_tax(base_info)

            self.save()

        except Exception as e:
            raise Exception(e)

    def calculate_monthly_wage(self):
        decree = Decree.objects.get(person=self.person, year=self.year)
        daily_wage = decree.base_salary
        monthly_wage = self.working_days * daily_wage

        return monthly_wage

    def calculate_overtime_wage(self):
        decree = Decree.objects.get(person=self.person, year=self.year)
        daily_wage = decree.base_salary
        overtime_wage = daily_wage / 7.33 * 1.4 * self.overtime

        return overtime_wage

    def calculate_closed_work_wage(self):
        decree = Decree.objects.get(person=self.person, year=self.year)
        daily_wage = decree.base_salary
        closed_work = daily_wage * 1.4 * self.closed_work

        return closed_work

    def sub_salary_and_benefits(self):
        pass

    def sub_total_wage_covered_by_insurance(self):
        list_items_included_in_insurance = [self.monthly_wage, self.overtime_wage, self.closed_work_wage,
                                            self.right_of_house]
        return sum(list_items_included_in_insurance)

    def sub_total_wage_covered_by_tax(self):
        list_items_included_in_tax = [self.monthly_wage, self.overtime_wage, self.closed_work_wage,
                                      self.right_of_house, self.right_of_children, self.right_of_grocery]
        return sum(list_items_included_in_tax)

    def calculate_insurance(self):
        sub_total_wage_covered_by_insurance = int(self.sub_total_wage_covered_by_insurance())
        insurance = (sub_total_wage_covered_by_insurance * 7) / 100
        self.insurance = insurance
        self.sub_total_deductions += insurance
        self.save()

    # work over on this function 
    def calculate_tax(self, base_info):
        print('base_info: ', base_info)
        try:
            tax_list = base_info.tax_table.all()
            sub_total_wage_covered_by_tax = int(self.sub_total_wage_covered_by_tax())
            tax = 0
            for i in tax_list:
                from_wage = i.from_wage
                to_wage = i.to_wage
                tax_percent = i.tax_percent
                print('tax table: ', i)
                if sub_total_wage_covered_by_tax >= from_wage <= to_wage:
                    tax += (sub_total_wage_covered_by_tax * tax_percent) / 100
                    print('tax in loop: ', tax)

            self.tax = tax
            print('tax org: ', tax)
            self.sub_total_deductions += tax
            self.save()
        except Exception as e:
            raise Exception(e)

    def collect_deductions(self):
        pass
