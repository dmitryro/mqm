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
from extra import ContentTypeRestrictedFileField

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
    supported_docs = ContentTypeRestrictedFileField(
        upload_to='zip',
        content_types=['application/zip'],
        max_upload_size=5242880
    )
    class Meta:
        verbose_name = 'mqm'
        verbose_name_plural = 'mqms'


class Question(models.Model):
    pass      

class MQMAdmin(admin.ModelAdmin):
    fieldsets = ((None, {'fields': ['contact_name','local_mind','due_date','status','supported_docs']}),)
    list_display = ('contact_name','local_mind','due_date','status','supported_docs')


admin.site.register(Mqm, MQMAdmin)



