from django.contrib import admin
from .models import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'company_type', 'object', 'accountant', 'created', 'is_active']
    # prepopulated_fields = {'slug': ('name',)}
