from django.contrib import admin
from .models import LocalMind, Person, Ethnicity


class LocalMindAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)


class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'telephone')


class EthnicityAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)


admin.site.register(LocalMind, LocalMindAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Ethnicity, EthnicityAdmin)
