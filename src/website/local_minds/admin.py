from django.contrib import admin
from .models import LocalMind, Ethnicity


class LocalMindAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)


class EthnicityAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)


admin.site.register(LocalMind, LocalMindAdmin)
admin.site.register(Ethnicity, EthnicityAdmin)
