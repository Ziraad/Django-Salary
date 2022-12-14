from django import forms
from django.utils.translation import gettext_lazy as _

from company.models import Company

COMPANY_TYPE = (
    ('Private', 'خصوصی'),
    ('Government', 'دولتی'),
)


class CompanyForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        # first call parent's constructor
        super(CompanyForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['name'].required = False
        self.fields['company_type'].required = False
        self.fields['object'].required = False
        self.fields['start_of_activity'].required = False
        self.fields['address'].required = False
        self.fields['logo'].required = False
        self.fields['description'].required = False

    # specify the name of model to use
    class Meta:
        model = Company
        # fields = "__all__"
        exclude = ['slug', 'accountant', 'is_active']
        labels = {
            'name': _('نام'),
            'company_type': _('نوع شرکت'),
            'logo': _('لوگو'),
            'object': _('موضوع فعالیت'),
            'start_of_activity': _('تاریخ شروع فعالیت'),
            'address': _('آدرس'),
            'description': _('توضیحات'),
        }
        help_texts = {
            'name': _('Some useful help text.'),
        }
        error_messages = {
            'name': {
                'max_length': _("از تعداد کارکترهای کمتری استفاده کنید!"),
            },
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'block w-full px-3 py-1.5 text-base font-normal text-gray-700 '
                                                    'bg-white bg-clip-padding border border-solid border-gray-300 '
                                                    'rounded transition ease-in-out m-0 focus:text-gray-700 '
                                                    'focus:bg-white focus:border-blue-600 focus:outline-none'}),
            'company_type': forms.Select(attrs={'class': 'block w-full px-3 py-1.5 text-base font-normal text-gray-700 '
                                                         'bg-white bg-clip-padding border border-solid border-gray-300 '
                                                         'rounded transition ease-in-out m-0 focus:text-gray-700 '
                                                         'focus:bg-white focus:border-blue-600 focus:outline-none'}),
            'object': forms.TextInput(
                attrs={'class': 'block w-full px-3 py-1.5 text-base font-normal text-gray-700 '
                                'bg-white bg-clip-padding border border-solid border-gray-300 '
                                'rounded transition ease-in-out m-0 focus:text-gray-700 '
                                'focus:bg-white focus:border-blue-600 focus:outline-none'}),
            'start_of_activity': forms.TextInput(attrs={'class': 'block w-full px-3 py-1.5 text-base font-normal '
                                                                 'text-gray-700 '
                                                                 'bg-white bg-clip-padding border border-solid '
                                                                 'border-gray-300 '
                                                                 'rounded transition ease-in-out m-0 '
                                                                 'focus:text-gray-700 focus:text-base '
                                                                 'focus:bg-white focus:border-blue-600 '
                                                                 'focus:outline-none',
                                                        'placeholder': '1401/01/01'}),
            'address': forms.TextInput(attrs={'class': 'block w-full px-3 py-1.5 text-base font-normal text-gray-700 '
                                                       'bg-white bg-clip-padding border border-solid border-gray-300 '
                                                       'rounded transition ease-in-out m-0 focus:text-gray-700 '
                                                       'focus:bg-white focus:border-blue-600 focus:outline-none'}),
            'description': forms.Textarea(
                attrs={'rows': 4, 'class': 'block w-full px-3 py-1.5 text-base font-normal text-gray-700 '
                                           'bg-white bg-clip-padding border border-solid border-gray-300 '
                                           'rounded transition ease-in-out m-0 focus:text-gray-700 '
                                           'focus:bg-white focus:border-blue-600 focus:outline-none'}),

        }

    # authors = forms.ModelMultipleChoiceField(queryset=Author.objects.all())

    def clean(self):

        # data from the form is fetched using super function
        super(CompanyForm, self).clean()

        # extract the username and text field from the data
        name = self.cleaned_data.get('name')
        object_company = self.cleaned_data.get('object')
        start_of_activity = self.cleaned_data.get('start_of_activity')

        # conditions to be met for the name length
        if len(name) < 2 or len(name) == 0:
            self._errors['name'] = self.error_class([
                'نام شرکت باید حداقل 2 کاراکتر باشد!'])
        if len(name) > 50:
            self._errors['name'] = self.error_class([
                'نام شرکت باید از 50 کاراکتر کمتر باشد!'])

        # conditions to be met for the object length
        if len(object_company) < 2 or len(object_company) == 0:
            self._errors['object'] = self.error_class([
                'موضوع فعالیت شرکت باید حداقل 2 کاراکتر باشد!'])
        if len(object_company) > 200:
            self._errors['object'] = self.error_class([
                'موضوع فعالیت شرکت باید کمتر از 200 کاراکتر باشد!'])

        if len(start_of_activity) <= 0:
            self._errors['start_of_activity'] = self.error_class([
                'تاریخ شروع فعالیت را وارد کنید!'])

        return self.cleaned_data
