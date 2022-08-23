from django.contrib import admin

from .models import Person


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['personnel_code', 'company', 'first_name', 'last_name']
    # prepopulated_fields = {'slug': ('personnel_code',)}
