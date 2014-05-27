from django.contrib import admin
from .models import Service


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'local_mind', 'type', 'users_count',)
    list_filter = ('type',)
    search_fields = ('name', 'local_mind__name',)


admin.site.register(Service, ServiceAdmin)
