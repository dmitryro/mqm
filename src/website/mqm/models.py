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
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Base(models.Model):

    STATUS_CHOICES = (
         _('Intern'),
         _('General'),
         _('Admin'),
         _('Super User'),
    )


    contact_name_id = models.ForeignKey('accounts.User')
    local_mind = models.ForeignKey('local_minds.LocalMind')
    due_date = models.DateField()

    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'

    MQM_CHOICES = (
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
    )

    status = models.CharField(max_length=2,
                                      choices=MQM_CHOICES,
                                      default=FRESHMAN)

    
    class Meta:
        verbose_name = _('mqm')
        verbose_name_plural = _('mqms')

    def __str__(self):
        return self.contact_name

    def __unicode__(self):
        return unicode(self.contact_name)


class MQMAdmin(admin.ModelAdmin):
    fieldsets = ((None, {'fields': ['contact_name_id','local_mind','due_date','status']}),)
    list_display = ('contact_name_id','local_mind','due_date','status')


admin.site.register(Base, MQMAdmin)



