from django import forms


class FreeSalaryForm(forms.Form):
    first_name = forms.CharField(label='نام', required=False, max_length=50,
                                 widget=forms.TextInput(
                                     attrs={'class': 'block w-full px-3 py-1.5 text-base font-normal text-gray-700 '
                                                     'bg-white bg-clip-padding border border-solid border-gray-300 '
                                                     'rounded transition ease-in-out m-0 focus:text-gray-700 '
                                                     'focus:bg-white focus:border-blue-600 focus:outline-none',
                                            'placeholder': 'نام'}))
    last_name = forms.CharField(label='نام خانوادگی', required=False, max_length=50,
                                widget=forms.TextInput(
                                    attrs={'class': 'block w-full px-3 py-1.5 text-base font-normal text-gray-700 '
                                                    'bg-white bg-clip-padding border border-solid border-gray-300 '
                                                    'rounded transition ease-in-out m-0 focus:text-gray-700 '
                                                    'focus:bg-white focus:border-blue-600 focus:outline-none',
                                           'placeholder': 'نام خانوادگی'}))
    month_name = forms.EmailField(label='ماه', max_length=50, required=False,
                                  widget=forms.TextInput(
                                      attrs={'class': 'block w-full px-3 py-1.5 text-base font-normal text-gray-700 '
                                                      'bg-white bg-clip-padding border border-solid border-gray-300 '
                                                      'rounded transition ease-in-out m-0 focus:text-gray-700 '
                                                      'focus:bg-white focus:border-blue-600 focus:outline-none',
                                             'placeholder': 'ماه'}))
    year = forms.CharField(label='سال', max_length=11, required=True,
                           widget=forms.TextInput(
                               attrs={'class': 'block w-full px-3 py-1.5 text-base font-normal text-gray-700 '
                                               'bg-white bg-clip-padding border border-solid border-gray-300 '
                                               'rounded transition ease-in-out m-0 focus:text-gray-700 '
                                               'focus:bg-white focus:border-blue-600 focus:outline-none',
                                      'placeholder': 'سال'}))
    working_days = forms.IntegerField(label='کارکرد',

                                      )
    overtime = forms.IntegerField(label='اضافه کاری',
                                  )
    closed_work = forms.IntegerField(label='تعطیل کاری',
                                     )
    mission = forms.IntegerField(label='مأموریت',
                                 )
