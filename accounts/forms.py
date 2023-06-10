from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import (AuthenticationForm, PasswordResetForm, SetPasswordForm)

from .models import UserBase


class UserLoginForm(AuthenticationForm):

    username = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'نام کاربری', 'id': 'login-username'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder': 'رمز عبور',
            'id': 'login-pwd',
        }
    ))


class RegistrationForm(forms.ModelForm):

    username = forms.CharField(
        label='نام کاربری', min_length=4, max_length=50, help_text='اجباری')
    email = forms.EmailField(label='ایمیل', max_length=100, help_text='اجباری', error_messages={
        'required': 'متأسفیم، وارد کردن ایمیل اجباری است!'})
    password = forms.CharField(label='رمز عبور', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='تکرار رمز عبور', widget=forms.PasswordInput)

    class Meta:
        model = UserBase
        fields = ('username', 'email',)

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = UserBase.objects.filter(username=username)
        if r.count():
            raise forms.ValidationError("کاربر با این نام کاربری از قبل موجود است.")
        return username

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('رمز عبور یکسان نیست.')
        return cd['password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if UserBase.objects.filter(email=email).exists():
            raise forms.ValidationError(
                'لطفاً از ایمیل دیگری استفاده کنید. این ایمیل از قبل وجود دارد.')
        return email

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['username'].widget.attrs.update(
        #     {'placeholder': 'نام کاربری'})
        self.fields['email'].widget.attrs.update(
            {'name': 'email', 'id': 'id_email'})
        # self.fields['password'].widget.attrs.update(
        #     {'placeholder': 'رمز عبور'})
        # self.fields['password2'].widget.attrs.update(
        #     {'placeholder': 'تکرار رمز عبور'})

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'block w-full px-3 py-1.5 text-base font-normal text-gray-700 ' \
                                                       'bg-white bg-clip-padding border border-solid border-gray-300 ' \
                                                       'rounded transition ease-in-out mt-1 mb-4 dark:border-gray-600 ' \
                                                       'dark:bg-gray-700 focus:border-purple-400 focus:outline-none ' \
                                                       'focus:shadow-outline-purple dark:text-gray-300 ' \
                                                       'dark:focus:shadow-outline-gray form-input'


class PwdResetForm(PasswordResetForm):

    email = forms.EmailField(max_length=254, widget=forms.TextInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'Email', 'id': 'form-email'}))

    def clean_email(self):
        email = self.cleaned_data['email']
        u = UserBase.objects.filter(email=email)
        if not u:
            raise forms.ValidationError(
                'Unfortunatley we can not find that email address')
        return email


class PwdResetConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label='New password', widget=forms.PasswordInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'New Password', 'id': 'form-newpass'}))
    new_password2 = forms.CharField(
        label='Repeat password', widget=forms.PasswordInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'New Password', 'id': 'form-new-pass2'}))


class UserEditForm(forms.ModelForm):

    email = forms.EmailField(
        label='Account email (can not be changed)', max_length=200, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3 text-gray-700 dark:text-gray-400', 'placeholder': 'email', 'id': 'form-email', 'readonly': 'readonly'}))

    user_name = forms.CharField(
        label='Firstname', min_length=4, max_length=50, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Username', 'id': 'form-firstname', 'readonly': 'readonly'}))

    first_name = forms.CharField(
        label='Username', min_length=4, max_length=50, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Firstname', 'id': 'form-lastname'}))

    class Meta:
        model = UserBase
        fields = ('email', 'username', 'first_name',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].required = True
        self.fields['email'].required = True
