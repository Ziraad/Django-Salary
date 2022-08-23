from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import UserBase


class UserBaseAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'username', 'created', 'last_login', 'is_active')
    list_display_links = ('email', 'first_name', 'last_name')
    readonly_fields = ('last_login', 'created')
    ordering = ('-created',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(UserBase, UserBaseAdmin)

