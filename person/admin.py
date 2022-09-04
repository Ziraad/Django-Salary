from django.contrib import admin

from .models import Person


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['personnel_code', 'company', 'first_name', 'last_name', 'is_active']
    # prepopulated_fields = {'slug': ('personnel_code',)}
