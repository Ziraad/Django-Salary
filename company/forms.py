from django import forms
from django.utils.translation import gettext_lazy as _

from company.models import Company

from django import forms
from jalali_date.fields import JalaliDateField, SplitJalaliDateTimeField
from jalali_date.widgets import AdminJalaliDateWidget, AdminSplitJalaliDateTime

COMPANY_TYPE = (
    ('Private', 'خصوصی'),
    ('Government', 'دولتی'),
)


class CompanyForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        # first call parent's constructor
        super(CompanyForm, self).__init__(*args, **kwargs)

        self.fields['start_of_activity'] = JalaliDateField(label=_('تاریخ شروع فعالیت'),  # date format is  "yyyy-mm-dd"
                                                           widget=AdminJalaliDateWidget
                                                           # optional, to use default datepicker
                                                           )
        # self.fields['start_of_activity'] = SplitJalaliDateTimeField(label=_('تاریخ شروع فعالیت'),
        #                                                             widget=AdminSplitJalaliDateTime
        #                                                             # required, for decompress DatetimeField to
        #                                                             # JalaliDateField and JalaliTimeField
        #                                                             )

        # you can added a "class" to this field for use your datepicker!
        self.fields['start_of_activity'].widget.attrs.update(
            {'class': 'jalali_date-date block w-full px-3 py-1.5 text-base font-normal text-gray-700 '
                      'bg-white dark:bg-gray-800 dark:text-gray-400 dark:border-gray-700 bg-clip-padding '
                      'border border-solid border-gray-300 rounded transition ease-in-out m-0 '
                      'focus:text-gray-700 dark:focus:text-gray-400 focus:bg-white focus:border-gray-900 '
                      'focus:outline-none dark:focus:bg-gray-700 dark:focus:border-gray-700'}),

        # self.fields['date_time'] = SplitJalaliDateTimeField(label=_('date time'),
        #                                                     widget=AdminSplitJalaliDateTime
        #                                                     # required, for decompress DatetimeField to
        #                                                     # JalaliDateField and JalaliTimeField
        #                                                     )
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
            'name': forms.TextInput(
                attrs={'class': 'block w-full px-3 py-1.5 text-base font-normal text-gray-700 '
                                'bg-white dark:bg-gray-800 dark:text-gray-400 dark:border-gray-700 bg-clip-padding '
                                'border border-solid border-gray-300 rounded transition ease-in-out m-0 '
                                'focus:text-gray-700 dark:focus:text-gray-400 focus:bg-white focus:border-gray-900 '
                                'focus:outline-none dark:focus:bg-gray-700 dark:focus:border-gray-700'}),
            'company_type': forms.Select(
                attrs={'class': 'block w-full px-3 py-1.5 text-base font-normal text-gray-700 '
                                'bg-white dark:bg-gray-800 dark:text-gray-400 dark:border-gray-700 bg-clip-padding '
                                'border border-solid border-gray-300 rounded transition ease-in-out m-0 '
                                'focus:text-gray-700 dark:focus:text-gray-400 focus:bg-white focus:border-gray-900 '
                                'focus:outline-none dark:focus:bg-gray-700 dark:focus:border-gray-700'}),
            'object': forms.TextInput(
                attrs={'class': 'block w-full px-3 py-1.5 text-base font-normal text-gray-700 '
                                'bg-white dark:bg-gray-800 dark:text-gray-400 dark:border-gray-700 bg-clip-padding '
                                'border border-solid border-gray-300 rounded transition ease-in-out m-0 '
                                'focus:text-gray-700 dark:focus:text-gray-400 focus:bg-white focus:border-gray-900 '
                                'focus:outline-none dark:focus:bg-gray-700 dark:focus:border-gray-700'}),

            'address': forms.TextInput(
                attrs={'class': 'block w-full px-3 py-1.5 text-base font-normal text-gray-700 '
                                'bg-white dark:bg-gray-800 dark:text-gray-400 dark:border-gray-700 bg-clip-padding '
                                'border border-solid border-gray-300 rounded transition ease-in-out m-0 '
                                'focus:text-gray-700 dark:focus:text-gray-400 focus:bg-white focus:border-gray-900 '
                                'focus:outline-none dark:focus:bg-gray-700 dark:focus:border-gray-700'}),
            'description': forms.Textarea(
                attrs={'rows': 4, 'class': 'block w-full px-3 py-1.5 text-base font-normal text-gray-700 '
                                           'bg-white dark:bg-gray-800 dark:text-gray-400 dark:border-gray-700 '
                                           'bg-clip-padding border border-solid border-gray-300 rounded transition '
                                           'ease-in-out m-0 focus:text-gray-700 dark:focus:text-gray-400 focus:bg-white'
                                           'focus:border-gray-900 focus:outline-none dark:focus:bg-gray-700 '
                                           'dark:focus:border-gray-700'}),

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

        # if len(start_of_activity) <= 0:
        #     self._errors['start_of_activity'] = self.error_class([
        #         'تاریخ شروع فعالیت را وارد کنید!'])

        return self.cleaned_data
