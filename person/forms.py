from django import forms

from django.utils.translation import gettext_lazy as _

from company.models import Company
from salary.models import Decree, TypeOfEmployment, SalaryReceipt
from .models import Person


class PersonForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        # first call parent's constructor
        self.request = kwargs.pop("request")  # store value of request
        print(self.request.user)
        super(PersonForm, self).__init__(*args, **kwargs)

        # there's a `fields` property now
        # self.fields['name'].required = False
        # self.fields['company_type'].required = False
        # self.fields['object'].required = False
        # self.fields['address'].required = False
        # self.fields['description'].required = False
        self.fields['company'].queryset = Company.objects.filter(accountant=self.request.user)

    def clean(self):
        print(self.request.user)  # request now available here also
        pass

    # specify the name of model to use
    class Meta:
        model = Person
        # fields = "__all__"
        exclude = ['is_active']
        labels = {
            'company': _('نام شرکت'),
            'personnel_code': _('کد پرسنلی'),
            'first_name': _('نام'),
            'last_name': _('نام خانوادگی'),
            'nation_code': _('کد ملی'),
            'image': _('عکس'),
            'date_of_birth': _('تاریخ تولد'),
            'place_of_birth': _('محل تولد'),
            'father_name': _('نام پدر'),
            'education_degree': _('مدرک تحصیلی'),
            'number_of_children': _('تعداد فرزندان'),
            'marital_status': _('وضعیت تأهل'),
        }

        widgets = {
            'company': forms.Select(
                attrs={'class': 'block w-full px-3 py-1.5 text-base font-normal text-gray-700 '
                                'bg-white dark:bg-gray-800 dark:text-gray-400 dark:border-gray-700 bg-clip-padding '
                                'border border-solid border-gray-300 rounded transition ease-in-out m-0 '
                                'focus:text-gray-700 dark:focus:text-gray-400 focus:bg-white focus:border-gray-900 '
                                'focus:outline-none dark:focus:bg-gray-700 dark:focus:border-gray-700'}),
            'personnel_code': forms.TextInput(
                attrs={'class': 'block w-full px-3 py-1.5 text-base font-normal text-gray-700 '
                                'bg-white dark:bg-gray-800 dark:text-gray-400 dark:border-gray-700 bg-clip-padding '
                                'border border-solid border-gray-300 rounded transition ease-in-out m-0 '
                                'focus:text-gray-700 dark:focus:text-gray-400 focus:bg-white focus:border-gray-900 '
                                'focus:outline-none dark:focus:bg-gray-700 dark:focus:border-gray-700'}),
            'first_name': forms.TextInput(
                attrs={'class': 'block w-full px-3 py-1.5 text-base font-normal text-gray-700 '
                                'bg-white dark:bg-gray-800 dark:text-gray-400 dark:border-gray-700 bg-clip-padding '
                                'border border-solid border-gray-300 rounded transition ease-in-out m-0 '
                                'focus:text-gray-700 dark:focus:text-gray-400 focus:bg-white focus:border-gray-900 '
                                'focus:outline-none dark:focus:bg-gray-700 dark:focus:border-gray-700'}),
            'last_name': forms.TextInput(
                attrs={'class': 'block w-full px-3 py-1.5 text-base font-normal text-gray-700 '
                                'bg-white dark:bg-gray-800 dark:text-gray-400 dark:border-gray-700 bg-clip-padding '
                                'border border-solid border-gray-300 rounded transition ease-in-out m-0 '
                                'focus:text-gray-700 dark:focus:text-gray-400 focus:bg-white focus:border-gray-900 '
                                'focus:outline-none dark:focus:bg-gray-700 dark:focus:border-gray-700'}),
            'nation_code': forms.TextInput(
                attrs={'class': 'block w-full px-3 py-1.5 text-base font-normal text-gray-700 '
                                'bg-white dark:bg-gray-800 dark:text-gray-400 dark:border-gray-700 bg-clip-padding '
                                'border border-solid border-gray-300 rounded transition ease-in-out m-0 '
                                'focus:text-gray-700 dark:focus:text-gray-400 focus:bg-white focus:border-gray-900 '
                                'focus:outline-none dark:focus:bg-gray-700 dark:focus:border-gray-700'}),
            # 'id_code': forms.TextInput(
            #     attrs={'class': 'block w-full px-3 py-1.5 text-base font-normal text-gray-700 '
            #                     'bg-white bg-clip-padding border border-solid border-gray-300 '
            #                     'rounded transition ease-in-out m-0 focus:text-gray-700 '
            #                     'focus:bg-white focus:border-blue-600 focus:outline-none'}),
            'date_of_birth': forms.TextInput(
                attrs={'class': 'block w-full px-3 py-1.5 text-base font-normal text-gray-700 '
                                'bg-white dark:bg-gray-800 dark:text-gray-400 dark:border-gray-700 bg-clip-padding '
                                'border border-solid border-gray-300 rounded transition ease-in-out m-0 '
                                'focus:text-gray-700 dark:focus:text-gray-400 focus:bg-white focus:border-gray-900 '
                                'focus:outline-none dark:focus:bg-gray-700 dark:focus:border-gray-700'}),
            'place_of_birth': forms.TextInput(
                attrs={'class': 'block w-full px-3 py-1.5 text-base font-normal text-gray-700 '
                                'bg-white dark:bg-gray-800 dark:text-gray-400 dark:border-gray-700 bg-clip-padding '
                                'border border-solid border-gray-300 rounded transition ease-in-out m-0 '
                                'focus:text-gray-700 dark:focus:text-gray-400 focus:bg-white focus:border-gray-900 '
                                'focus:outline-none dark:focus:bg-gray-700 dark:focus:border-gray-700'}),
            'father_name': forms.TextInput(
                attrs={'class': 'block w-full px-3 py-1.5 text-base font-normal text-gray-700 '
                                'bg-white dark:bg-gray-800 dark:text-gray-400 dark:border-gray-700 bg-clip-padding '
                                'border border-solid border-gray-300 rounded transition ease-in-out m-0 '
                                'focus:text-gray-700 dark:focus:text-gray-400 focus:bg-white focus:border-gray-900 '
                                'focus:outline-none dark:focus:bg-gray-700 dark:focus:border-gray-700'}),
            'education_degree': forms.TextInput(
                attrs={'class': 'block w-full px-3 py-1.5 text-base font-normal text-gray-700 '
                                'bg-white dark:bg-gray-800 dark:text-gray-400 dark:border-gray-700 bg-clip-padding '
                                'border border-solid border-gray-300 rounded transition ease-in-out m-0 '
                                'focus:text-gray-700 dark:focus:text-gray-400 focus:bg-white focus:border-gray-900 '
                                'focus:outline-none dark:focus:bg-gray-700 dark:focus:border-gray-700'}),
            'number_of_children': forms.TextInput(
                attrs={'class': 'block w-full px-3 py-1.5 text-base font-normal text-gray-700 '
                                'bg-white dark:bg-gray-800 dark:text-gray-400 dark:border-gray-700 bg-clip-padding '
                                'border border-solid border-gray-300 rounded transition ease-in-out m-0 '
                                'focus:text-gray-700 dark:focus:text-gray-400 focus:bg-white focus:border-gray-900 '
                                'focus:outline-none dark:focus:bg-gray-700 dark:focus:border-gray-700'}),
            'marital_status': forms.Select(
                attrs={'class': 'block w-full px-3 py-1.5 text-base font-normal text-gray-700 '
                                'bg-white dark:bg-gray-800 dark:text-gray-400 dark:border-gray-700 bg-clip-padding '
                                'border border-solid border-gray-300 rounded transition ease-in-out m-0 '
                                'focus:text-gray-700 dark:focus:text-gray-400 focus:bg-white focus:border-gray-900 '
                                'focus:outline-none dark:focus:bg-gray-700 dark:focus:border-gray-700'}),

        }

    # authors = forms.ModelMultipleChoiceField(queryset=Author.objects.all())

    # def clean(self):
    #
    #     # data from the form is fetched using super function
    #     super(PersonForm, self).clean()
    #
    #     # extract the username and text field from the data
    #     name = self.cleaned_data.get('name')
    #     object_company = self.cleaned_data.get('object')
    #
    #     # conditions to be met for the name length
    #     if len(name) < 2 or len(name) == 0:
    #         self._errors['name'] = self.error_class([
    #             'نام شرکت باید حداقل 2 کاراکتر باشد!'])
    #     if len(name) > 50:
    #         self._errors['name'] = self.error_class([
    #             'نام شرکت باید از 50 کاراکتر کمتر باشد!'])
    #
    #     # conditions to be met for the object length
    #     if len(object_company) < 2 or len(object_company) == 0:
    #         self._errors['object'] = self.error_class([
    #             'موضوع فعالیت شرکت باید حداقل 2 کاراکتر باشد!'])
    #     if len(object_company) > 200:
    #         self._errors['object'] = self.error_class([
    #             'موضوع فعالیت شرکت باید کمتر از 200 کاراکتر باشد!'])
    #
    #     return self.cleaned_data


class DecreeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        # first call parent's constructor
        self.request = kwargs.pop("request")  # store value of request
        # personal_code = kwargs.pop("slug")  # store value of request
        print(self.request.user)
        # print(personal_code)
        super(DecreeForm, self).__init__(*args, **kwargs)
        self.fields['company'].queryset = Company.objects.filter(accountant=self.request.user)
        # if personal_code:
        #     self.fields['person'].queryset = Person.objects.filter(personnel_code=personal_code)
        # else:
        self.fields['person'].queryset = Person.objects.filter(company__accountant=self.request.user)

        # there's a `fields` property now
        self.fields['company'].required = True
        self.fields['person'].required = True
        self.fields['type_of_rule'].required = True
        self.fields['type_of_employment'].required = True
        self.fields['year'].required = False
        self.fields['base_salary'].required = False
        self.fields['right_of_children'].required = False
        self.fields['right_to_housing'].required = False
        self.fields['right_to_grocery'].required = False
        self.fields['job_title'].required = False
        self.fields['date_of_hire'].required = False
        # self.fields['description'].required = False

    class Meta:
        model = Decree
        # fields = "__all__"
        exclude = ['created_by']
        labels = {
            'company': _('نام شرکت*'),
            'person': _('پرسنل*'),
            'year': _('سال*'),
            'type_of_rule': _('نوع حکم*'),
            'type_of_employment': _('نوع استخدام*'),
            'base_salary': _('حقوق پایه(روزانه)*'),
            'base_years': _('پایه سنوات(روزانه)'),
            'reward': _('پاداش'),
            'right_to_housing': _('حق مسکن(ماهانه)*'),
            'right_to_grocery': _('حق خوار و بار(ماهانه)*'),
            'right_to_supervisor': _('حق سرپرستی(روزانه)'),
            'right_of_children': _('حق اولاد(ماهانه)*'),
            'service_location': _('محل خدمت'),
            'job_title': _('عنوان شغلی*'),
            'date_of_hire': _('تاریخ استخدام*'),
        }

        widgets = {
            'company': forms.Select(
                attrs={'class': 'block w-full px-3 py-1.5 text-base font-normal text-gray-700 '
                                'bg-white dark:bg-gray-800 dark:text-gray-400 dark:border-gray-700 bg-clip-padding '
                                'border border-solid border-gray-300 rounded transition ease-in-out m-0 '
                                'focus:text-gray-700 dark:focus:text-gray-400 focus:bg-white focus:border-gray-900 '
                                'focus:outline-none dark:focus:bg-gray-700 dark:focus:border-gray-700'}),
            'person': forms.Select(
                attrs={'class': 'block w-full px-3 py-1.5 text-base font-normal text-gray-700 '
                                'bg-white dark:bg-gray-800 dark:text-gray-400 dark:border-gray-700 bg-clip-padding '
                                'border border-solid border-gray-300 rounded transition ease-in-out m-0 '
                                'focus:text-gray-700 dark:focus:text-gray-400 focus:bg-white focus:border-gray-900 '
                                'focus:outline-none dark:focus:bg-gray-700 dark:focus:border-gray-700'}),
            'year': forms.TextInput(
                attrs={'class': 'block w-full px-3 py-1.5 text-base font-normal text-gray-700 '
                                'bg-white dark:bg-gray-800 dark:text-gray-400 dark:border-gray-700 bg-clip-padding '
                                'border border-solid border-gray-300 rounded transition ease-in-out m-0 '
                                'focus:text-gray-700 dark:focus:text-gray-400 focus:bg-white focus:border-gray-900 '
                                'focus:outline-none dark:focus:bg-gray-700 dark:focus:border-gray-700'}),
            'type_of_rule': forms.Select(
                attrs={'class': 'block w-full px-3 py-1.5 text-base font-normal text-gray-700 '
                                'bg-white dark:bg-gray-800 dark:text-gray-400 dark:border-gray-700 bg-clip-padding '
                                'border border-solid border-gray-300 rounded transition ease-in-out m-0 '
                                'focus:text-gray-700 dark:focus:text-gray-400 focus:bg-white focus:border-gray-900 '
                                'focus:outline-none dark:focus:bg-gray-700 dark:focus:border-gray-700'}),
            'type_of_employment': forms.Select(
                attrs={'class': 'block w-full px-3 py-1.5 text-base font-normal text-gray-700 '
                                'bg-white dark:bg-gray-800 dark:text-gray-400 dark:border-gray-700 bg-clip-padding '
                                'border border-solid border-gray-300 rounded transition ease-in-out m-0 '
                                'focus:text-gray-700 dark:focus:text-gray-400 focus:bg-white focus:border-gray-900 '
                                'focus:outline-none dark:focus:bg-gray-700 dark:focus:border-gray-700'}),
            'base_salary': forms.TextInput(
                attrs={'class': 'block w-full px-3 py-1.5 text-base font-normal text-gray-700 '
                                'bg-white dark:bg-gray-800 dark:text-gray-400 dark:border-gray-700 bg-clip-padding '
                                'border border-solid border-gray-300 rounded transition ease-in-out m-0 '
                                'focus:text-gray-700 dark:focus:text-gray-400 focus:bg-white focus:border-gray-900 '
                                'focus:outline-none dark:focus:bg-gray-700 dark:focus:border-gray-700'}),
            'base_years': forms.TextInput(
                attrs={'class': 'block w-full px-3 py-1.5 text-base font-normal text-gray-700 '
                                'bg-white dark:bg-gray-800 dark:text-gray-400 dark:border-gray-700 bg-clip-padding '
                                'border border-solid border-gray-300 rounded transition ease-in-out m-0 '
                                'focus:text-gray-700 dark:focus:text-gray-400 focus:bg-white focus:border-gray-900 '
                                'focus:outline-none dark:focus:bg-gray-700 dark:focus:border-gray-700'}),
            'reward': forms.TextInput(
                attrs={'class': 'block w-full px-3 py-1.5 text-base font-normal text-gray-700 '
                                'bg-white dark:bg-gray-800 dark:text-gray-400 dark:border-gray-700 bg-clip-padding '
                                'border border-solid border-gray-300 rounded transition ease-in-out m-0 '
                                'focus:text-gray-700 dark:focus:text-gray-400 focus:bg-white focus:border-gray-900 '
                                'focus:outline-none dark:focus:bg-gray-700 dark:focus:border-gray-700'}),
            'right_to_housing': forms.TextInput(
                attrs={'class': 'block w-full px-3 py-1.5 text-base font-normal text-gray-700 '
                                'bg-white dark:bg-gray-800 dark:text-gray-400 dark:border-gray-700 bg-clip-padding '
                                'border border-solid border-gray-300 rounded transition ease-in-out m-0 '
                                'focus:text-gray-700 dark:focus:text-gray-400 focus:bg-white focus:border-gray-900 '
                                'focus:outline-none dark:focus:bg-gray-700 dark:focus:border-gray-700'}),
            'right_to_grocery': forms.TextInput(
                attrs={'class': 'block w-full px-3 py-1.5 text-base font-normal text-gray-700 '
                                'bg-white dark:bg-gray-800 dark:text-gray-400 dark:border-gray-700 bg-clip-padding '
                                'border border-solid border-gray-300 rounded transition ease-in-out m-0 '
                                'focus:text-gray-700 dark:focus:text-gray-400 focus:bg-white focus:border-gray-900 '
                                'focus:outline-none dark:focus:bg-gray-700 dark:focus:border-gray-700'}),
            'right_of_children': forms.TextInput(
                attrs={'class': 'block w-full px-3 py-1.5 text-base font-normal text-gray-700 '
                                'bg-white dark:bg-gray-800 dark:text-gray-400 dark:border-gray-700 bg-clip-padding '
                                'border border-solid border-gray-300 rounded transition ease-in-out m-0 '
                                'focus:text-gray-700 dark:focus:text-gray-400 focus:bg-white focus:border-gray-900 '
                                'focus:outline-none dark:focus:bg-gray-700 dark:focus:border-gray-700'}),
            'right_to_supervisor': forms.TextInput(
                attrs={'class': 'block w-full px-3 py-1.5 text-base font-normal text-gray-700 '
                                'bg-white dark:bg-gray-800 dark:text-gray-400 dark:border-gray-700 bg-clip-padding '
                                'border border-solid border-gray-300 rounded transition ease-in-out m-0 '
                                'focus:text-gray-700 dark:focus:text-gray-400 focus:bg-white focus:border-gray-900 '
                                'focus:outline-none dark:focus:bg-gray-700 dark:focus:border-gray-700'}),
            'service_location': forms.TextInput(
                attrs={'class': 'block w-full px-3 py-1.5 text-base font-normal text-gray-700 '
                                'bg-white dark:bg-gray-800 dark:text-gray-400 dark:border-gray-700 bg-clip-padding '
                                'border border-solid border-gray-300 rounded transition ease-in-out m-0 '
                                'focus:text-gray-700 dark:focus:text-gray-400 focus:bg-white focus:border-gray-900 '
                                'focus:outline-none dark:focus:bg-gray-700 dark:focus:border-gray-700'}),
            'job_title': forms.TextInput(
                attrs={'class': 'block w-full px-3 py-1.5 text-base font-normal text-gray-700 '
                                'bg-white dark:bg-gray-800 dark:text-gray-400 dark:border-gray-700 bg-clip-padding '
                                'border border-solid border-gray-300 rounded transition ease-in-out m-0 '
                                'focus:text-gray-700 dark:focus:text-gray-400 focus:bg-white focus:border-gray-900 '
                                'focus:outline-none dark:focus:bg-gray-700 dark:focus:border-gray-700'}),
            'date_of_hire': forms.TextInput(
                attrs={'class': 'myclass block w-full px-3 py-1.5 text-sm font-normal text-gray-700 '
                                'bg-white dark:bg-gray-800 dark:text-gray-400 dark:border-gray-700 bg-clip-padding '
                                'border border-solid border-gray-300 rounded transition ease-in-out m-0 '
                                'focus:text-gray-700 dark:focus:text-gray-400 focus:bg-white focus:border-gray-900 '
                                'focus:outline-none dark:focus:bg-gray-700 dark:focus:border-gray-700',
                       'id': 'mydate'}),
        }
        type_of_employment = forms.ModelMultipleChoiceField(queryset=TypeOfEmployment.objects.all())


class SalaryReceiptForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        # first call parent's constructor
        self.request = kwargs.pop("request")  # store value of request
        print(self.request.user)
        super(SalaryReceiptForm, self).__init__(*args, **kwargs)
        # self.fields['company'].queryset = Company.objects.filter(accountant=self.request.user)
        self.fields['person'].queryset = Person.objects.filter(company__accountant=self.request.user)

        # there's a `fields` property now
        self.fields['person'].required = True
        self.fields['month_name'].required = True
        self.fields['year'].required = False
        self.fields['working_days'].required = False
        self.fields['overtime'].required = False
        self.fields['closed_work'].required = False
        self.fields['mission'].required = False

    class Meta:
        model = SalaryReceipt
        # fields = "__all__"
        exclude = ['created_by', 'monthly_wage', 'overtime_wage', 'closed_work_wage', 'mission_wage', 'right_of_house',
                   'right_of_grocery', 'right_of_children', 'sub_total_wage']
        labels = {
            'person': _('نام پرسنل'),
            'month_name': _('ماه'),
            'year': _('سال'),
            'working_days': _('کارکرد روزانه'),
            'overtime': _('اضافه کاری'),
            'closed_work': _('تعطیل کاری'),
            'mission': _('مأموریت'),
        }

        widgets = {
            'person': forms.Select(
                attrs={'class': 'block w-full px-3 py-1.5 text-base font-normal text-gray-700 '
                                'bg-white dark:bg-gray-800 dark:text-gray-400 dark:border-gray-700 bg-clip-padding '
                                'border border-solid border-gray-300 rounded transition ease-in-out m-0 '
                                'focus:text-gray-700 dark:focus:text-gray-400 focus:bg-white focus:border-gray-900 '
                                'focus:outline-none dark:focus:bg-gray-700 dark:focus:border-gray-700'}),
            'month_name': forms.Select(
                attrs={'class': 'block w-full px-3 py-1.5 text-base font-normal text-gray-700 '
                                'bg-white dark:bg-gray-800 dark:text-gray-400 dark:border-gray-700 bg-clip-padding '
                                'border border-solid border-gray-300 rounded transition ease-in-out m-0 '
                                'focus:text-gray-700 dark:focus:text-gray-400 focus:bg-white focus:border-gray-900 '
                                'focus:outline-none dark:focus:bg-gray-700 dark:focus:border-gray-700'}),
            'year': forms.TextInput(
                attrs={'class': 'block w-full px-3 py-1.5 text-base font-normal text-gray-700 '
                                'bg-white dark:bg-gray-800 dark:text-gray-400 dark:border-gray-700 bg-clip-padding '
                                'border border-solid border-gray-300 rounded transition ease-in-out m-0 '
                                'focus:text-gray-700 dark:focus:text-gray-400 focus:bg-white focus:border-gray-900 '
                                'focus:outline-none dark:focus:bg-gray-700 dark:focus:border-gray-700'}),
            'working_days': forms.TextInput(
                attrs={'class': 'block w-full px-3 py-1.5 text-base font-normal text-gray-700 '
                                'bg-white dark:bg-gray-800 dark:text-gray-400 dark:border-gray-700 bg-clip-padding '
                                'border border-solid border-gray-300 rounded transition ease-in-out m-0 '
                                'focus:text-gray-700 dark:focus:text-gray-400 focus:bg-white focus:border-gray-900 '
                                'focus:outline-none dark:focus:bg-gray-700 dark:focus:border-gray-700'}),
            'overtime': forms.TextInput(
                attrs={'class': 'block w-full px-3 py-1.5 text-base font-normal text-gray-700 '
                                'bg-white dark:bg-gray-800 dark:text-gray-400 dark:border-gray-700 bg-clip-padding '
                                'border border-solid border-gray-300 rounded transition ease-in-out m-0 '
                                'focus:text-gray-700 dark:focus:text-gray-400 focus:bg-white focus:border-gray-900 '
                                'focus:outline-none dark:focus:bg-gray-700 dark:focus:border-gray-700'}),
            'closed_work': forms.TextInput(
                attrs={'class': 'block w-full px-3 py-1.5 text-base font-normal text-gray-700 '
                                'bg-white dark:bg-gray-800 dark:text-gray-400 dark:border-gray-700 bg-clip-padding '
                                'border border-solid border-gray-300 rounded transition ease-in-out m-0 '
                                'focus:text-gray-700 dark:focus:text-gray-400 focus:bg-white focus:border-gray-900 '
                                'focus:outline-none dark:focus:bg-gray-700 dark:focus:border-gray-700'}),
            'mission': forms.TextInput(
                attrs={'class': 'block w-full px-3 py-1.5 text-base font-normal text-gray-700 '
                                'bg-white dark:bg-gray-800 dark:text-gray-400 dark:border-gray-700 bg-clip-padding '
                                'border border-solid border-gray-300 rounded transition ease-in-out m-0 '
                                'focus:text-gray-700 dark:focus:text-gray-400 focus:bg-white focus:border-gray-900 '
                                'focus:outline-none dark:focus:bg-gray-700 dark:focus:border-gray-700'}),
        }
