# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.auth.models import Group as _Group
from django.utils.translation import ugettext_lazy as _

from ..tasks.models import Task
from .models import User, Experience, Group, ReservedEmail, Skill


class ExperienceAdminInline(admin.TabularInline):
    model = Experience
    extra = 0


class TaskAdminInline(admin.StackedInline):
    model = Task
    fk_name = 'assigned_to'
    extra = 0


class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'local_mind', 'is_active', 'is_staff', 'is_superuser', 'privileges', 'date_joined',)
    list_filter = ('is_active', 'is_staff', 'privileges',)
    date_hierarchy = 'date_joined'
    search_fields = ('email', 'first_name', 'last_name', 'local_mind__name')
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
                'user_avatar',
                'telephone',
            ),
        }),
        (_('Administration'), {
            'classes': ('wide',),
            'fields': (
                'local_mind',
                'privileges',
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
    inlines = [ExperienceAdminInline, TaskAdminInline]


class GroupAdmin(admin.ModelAdmin):
    pass


class ReservedEmailAdmin(admin.ModelAdmin):
    list_display = ('email', 'local_mind',)
    search_fields = ('email',)


admin.site.register(User, UserAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(ReservedEmail, ReservedEmailAdmin)
admin.site.register(Skill)

admin.site.unregister(_Group)
