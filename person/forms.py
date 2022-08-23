from django import forms

from django.utils.translation import gettext_lazy as _

from company.models import Company
from .models import Person


class PersonForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        # first call parent's constructor
        super(PersonForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        # self.fields['name'].required = False
        # self.fields['company_type'].required = False
        # self.fields['object'].required = False
        # self.fields['address'].required = False
        # self.fields['description'].required = False

        # self.fields['company'].queryset = Company.objects.filter(accountant=user)

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
            'company': forms.Select(attrs={'class': 'block w-full px-3 py-1.5 text-base font-normal text-gray-700 '
                                                    'bg-white bg-clip-padding border border-solid border-gray-300 '
                                                    'rounded transition ease-in-out m-0 focus:text-gray-700 '
                                                    'focus:bg-white focus:border-blue-600 focus:outline-none'}),
            'personnel_code': forms.TextInput(attrs={'class': 'block w-full px-3 py-1.5 text-base font-normal '
                                                              'text-gray-700 '
                                                              'bg-white bg-clip-padding border border-solid '
                                                              'border-gray-300 '
                                                              'rounded transition ease-in-out m-0 focus:text-gray-700 '
                                                              'focus:bg-white focus:border-blue-600 focus:outline-none'}),
            'first_name': forms.TextInput(
                attrs={'class': 'block w-full px-3 py-1.5 text-base font-normal text-gray-700 '
                                'bg-white bg-clip-padding border border-solid border-gray-300 '
                                'rounded transition ease-in-out m-0 focus:text-gray-700 '
                                'focus:bg-white focus:border-blue-600 focus:outline-none'}),
            'last_name': forms.TextInput(attrs={'class': 'block w-full px-3 py-1.5 text-base font-normal text-gray-700 '
                                                         'bg-white bg-clip-padding border border-solid border-gray-300 '
                                                         'rounded transition ease-in-out m-0 focus:text-gray-700 '
                                                         'focus:bg-white focus:border-blue-600 focus:outline-none'}),
            'nation_code': forms.TextInput(
                attrs={'class': 'block w-full px-3 py-1.5 text-base font-normal text-gray-700 '
                                'bg-white bg-clip-padding border border-solid border-gray-300 '
                                'rounded transition ease-in-out m-0 focus:text-gray-700 '
                                'focus:bg-white focus:border-blue-600 focus:outline-none'}),
            # 'id_code': forms.TextInput(
            #     attrs={'class': 'block w-full px-3 py-1.5 text-base font-normal text-gray-700 '
            #                     'bg-white bg-clip-padding border border-solid border-gray-300 '
            #                     'rounded transition ease-in-out m-0 focus:text-gray-700 '
            #                     'focus:bg-white focus:border-blue-600 focus:outline-none'}),
            'date_of_birth': forms.TextInput(
                attrs={'class': 'block w-full px-3 py-1.5 text-base font-normal text-gray-700 '
                                'bg-white bg-clip-padding border border-solid border-gray-300 '
                                'rounded transition ease-in-out m-0 focus:text-gray-700 '
                                'focus:bg-white focus:border-blue-600 focus:outline-none'}),
            'place_of_birth': forms.TextInput(
                attrs={'class': 'block w-full px-3 py-1.5 text-base font-normal text-gray-700 '
                                'bg-white bg-clip-padding border border-solid border-gray-300 '
                                'rounded transition ease-in-out m-0 focus:text-gray-700 '
                                'focus:bg-white focus:border-blue-600 focus:outline-none'}),
            'father_name': forms.TextInput(
                attrs={'class': 'block w-full px-3 py-1.5 text-base font-normal text-gray-700 '
                                'bg-white bg-clip-padding border border-solid border-gray-300 '
                                'rounded transition ease-in-out m-0 focus:text-gray-700 '
                                'focus:bg-white focus:border-blue-600 focus:outline-none'}),
            'education_degree': forms.TextInput(
                attrs={'class': 'block w-full px-3 py-1.5 text-base font-normal text-gray-700 '
                                'bg-white bg-clip-padding border border-solid border-gray-300 '
                                'rounded transition ease-in-out m-0 focus:text-gray-700 '
                                'focus:bg-white focus:border-blue-600 focus:outline-none'}),
            'number_of_children': forms.TextInput(
                attrs={'class': 'block w-full px-3 py-1.5 text-base font-normal text-gray-700 '
                                'bg-white bg-clip-padding border border-solid border-gray-300 '
                                'rounded transition ease-in-out m-0 focus:text-gray-700 '
                                'focus:bg-white focus:border-blue-600 focus:outline-none'}),
            'marital_status': forms.Select(
                attrs={'class': 'block w-full px-3 py-1.5 text-base font-normal text-gray-700 '
                                'bg-white bg-clip-padding border border-solid border-gray-300 '
                                'rounded transition ease-in-out m-0 focus:text-gray-700 '
                                'focus:bg-white focus:border-blue-600 focus:outline-none'}),

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
