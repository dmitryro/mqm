from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import Resource


class ResourceAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'local_mind', 'user', 'privacy',)
    list_filter = ('privacy',)


admin.site.register(Resource, ResourceAdmin)
