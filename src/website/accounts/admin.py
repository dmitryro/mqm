# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.auth.models import Group as _Group
from django.utils.translation import ugettext_lazy as _

from .models import User, Group


class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_active', 'is_staff', 'is_superuser', 'date_joined',)
    list_filter = ('is_active', 'is_staff',)
    date_hierarchy = 'date_joined'
    search_fields = ('email', 'first_name', 'last_name',)
    filter_horizontal = ('user_permissions', 'groups')
    ordering = ('date_joined',)
    fieldsets = (
        (_('Account data'), {
            'classes': ('wide',),
            'fields': (
                'email',
                'first_name',
                'last_name',
                'job_title',
                'image',
                'telephone',
            ),
        }),
        (_('Administration'), {
            'classes': ('wide',),
            'fields': (
                'is_active',
                'is_staff',
                'date_joined',
            ),
        }),
        (_('Permissions'), {
            'classes': ('wide',),
            'fields': (
                'is_superuser',
                'groups',
                'user_permissions',
            ),
        }),
    )


class GroupAdmin(admin.ModelAdmin):
    pass


admin.site.register(User, UserAdmin)
admin.site.register(Group, GroupAdmin)

admin.site.unregister(_Group)
