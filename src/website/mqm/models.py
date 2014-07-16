"""
  MQM model
  July 2014 
"""
from django.db import models
from django.contrib import admin
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.utils.http import int_to_base36
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.fields import AutoSlugField
from mediastore.fields import MediaField, MultipleMediaField

"""
MQM Model class
"""
class Mqm(models.Model):

    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'

    MQM_CHOICES = (
        (FRESHMAN,'Freshman'),
        (SOPHOMORE,'Sophomore'),
        (JUNIOR,'Junior'),
        (SENIOR,'Senior'),
    )

    contact_name = models.ForeignKey('accounts.User', verbose_name='contact name')
    local_mind = models.ForeignKey('local_minds.LocalMind')
    due_date = models.DateField()
    status = models.CharField(max_length=2,choices=MQM_CHOICES,default=FRESHMAN)

    class Meta:
        verbose_name = 'mqm'
        verbose_name_plural = 'mqms'

class Question(models.Model):
    pass      

class MQMAdmin(admin.ModelAdmin):
    fieldsets = ((None, {'fields': ['contact_name','local_mind','due_date','status']}),)
    list_display = ('contact_name','local_mind','due_date','status')


admin.site.register(Mqm, MQMAdmin)



