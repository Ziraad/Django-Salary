from django.contrib import admin

from .models import Warrant, SalaryReceipt, TypeOfEmployment, BaseInfo


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


admin.site.register(Warrant)
admin.site.register(SalaryReceipt)
