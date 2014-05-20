from django.contrib import admin
from .models import LocalMind


class LocalMindAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)


admin.site.register(LocalMind, LocalMindAdmin)
