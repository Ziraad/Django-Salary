from django.contrib import admin

from .models import Decree, SalaryReceipt, TypeOfEmployment, BaseInfo


@admin.register(BaseInfo)
class BaseInfoAdmin(admin.ModelAdmin):
    list_display = ('year', 'base_salary', 'base_years', 'right_to_housing', 'right_to_grocery', 'right_to_children',
                    'created')
    list_editable = ['base_salary', 'base_years', 'right_to_housing', 'right_to_grocery', 'right_to_children']
    ordering = ('-created',)


@admin.register(TypeOfEmployment)
class TypeOfEmploymentAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}
    list_display_links = ('name',)


@admin.register(SalaryReceipt)
class TypeOfEmploymentAdmin(admin.ModelAdmin):
    list_display = ['person', 'month_name', 'year', 'created_by', 'created']


admin.site.register(Decree)
# admin.site.register(SalaryReceipt)
