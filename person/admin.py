from django.contrib import admin

from .models import Person

from jalali_date import admin as j_admin, datetime2jalali, date2jalali
from jalali_date.admin import ModelAdminJalaliMixin, StackedInlineJalaliMixin, TabularInlineJalaliMixin


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['personnel_code', 'company', 'first_name', 'last_name', 'is_active', 'get_created_jalali']
    # prepopulated_fields = {'slug': ('name',)}
    # raw_id_fields = ('some_fields',)
    # readonly_fields = ('some_fields', 'date_field',)
    # you can override formfield, for example:
    # formfield_overrides = {
    #     JSONField: {'widget': JSONEditor},
    # }

    @admin.display(description='تاریخ ایجاد', ordering='created')
    def get_created_jalali(self, obj):
        return date2jalali(obj.created).strftime('%a, %d %b %Y %H:%M:%S')