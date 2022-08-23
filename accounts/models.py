from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.core.mail import send_mail
from django.db import models
from django.utils.translation import gettext_lazy as _

from company.models import Company


class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, username, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, username, password, **other_fields)

    def create_user(self, email, username, password, **other_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, username=username,
                          **other_fields)
        user.set_password(password)
        user.save()
        return user


class UserBase(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(_('آدرس ایمیل'), unique=True)
    username = models.CharField('نام کاربری', max_length=150, unique=True)
    first_name = models.CharField('نام', max_length=150, blank=True)
    last_name = models.CharField('نام خانوادگی', max_length=150, blank=True)
    image = models.ImageField(upload_to='img/profiles', default='img/profiles/default.png', blank=True)
    about = models.TextField(_(
        'درباره'), max_length=500, blank=True)
    # Delivery details
    phone_number = models.CharField('موبایل', max_length=15, blank=True)
    postcode = models.CharField('کد پستی', max_length=12, blank=True)
    address_line_1 = models.CharField('آدرس', max_length=150, blank=True)
    address_line_2 = models.CharField('ادامه آدرس', max_length=150, blank=True)
    town_city = models.CharField('شهر', max_length=150, blank=True)
    # User Status
    is_active = models.BooleanField('فعال', default=False)
    is_staff = models.BooleanField('کارمند', default=False)
    created = models.DateTimeField('ایجاد شده در', auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    last_login = models.DateTimeField('آخرین فعالیت', auto_now_add=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = "نمایه کاربری"
        verbose_name_plural = "نمایه کاربری"

    def email_user(self, subject, message):
        send_mail(
            subject,
            message,
            'l@1.com',
            [self.email],
            fail_silently=False,
        )

    def __str__(self):
        return self.username
