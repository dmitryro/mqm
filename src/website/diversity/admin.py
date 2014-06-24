from django.contrib import admin
from .models import Diversity


class DiversityAdmin(admin.ModelAdmin):
    list_display = ('trustees_white_british',)

admin.site.register(Diversity, DiversityAdmin)
