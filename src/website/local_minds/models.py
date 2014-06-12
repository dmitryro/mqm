from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.fields import AutoSlugField, CreationDateTimeField, ModificationDateTimeField


class ReservedLocalMind(models.Model):
    name = models.CharField(_('Local Mind'), max_length=120)

    class Meta:
        verbose_name = _('Reserved Local Mind')
        verbose_name_plural = _('Reserved Local Minds')

    def __unicode__(self):
        return self.name


class LocalMind(models.Model):
    CHARITY_TYPE_CHOICES = (
        ('unincorporated', _('Unincorporated'),),
        ('company-limited-by-guarantee', _('Company Limited by Guarantee'),),
        ('charitable-incorporated-organisation', _('Charitable Incorporated Organisation'),),
    )

    REGION_CHOICES = (
        ('east-of-england', _('East of England')),
        ('east-midlands', _('East Midlands')),
        ('london', _('London')),
        ('north-east', _('North East')),
        ('north-west', _('North West')),
        ('south-east', _('South East')),
        ('south-west', _('South West')),
        ('wales', _('Wales')),
        ('west-midlands', _('West Midlands')),
        ('yorkshire-and-the-humber', _('Yorkshire and The Humber')),
    )

    reserved_local_mind = models.OneToOneField('ReservedLocalMind', null=True, blank=True)
    name = models.CharField(_('Local Mind'), max_length=120)
    slug = AutoSlugField(populate_from=('name',))

    region = models.CharField(_('Region'), max_length=50, choices=REGION_CHOICES, blank=True)
    address = models.TextField(_('Address'), blank=True)
    postcode = models.CharField(_('Postcode'), max_length=50, blank=True)
    income_restricted = models.CharField(_('LM Income R'), max_length=50, blank=True)
    income_unrestricted = models.CharField(_('LM Income U'), max_length=50, blank=True)
    charity_no = models.CharField(_('Charity Number'), max_length=30, blank=True)
    charity_type = models.CharField(_('Charity Type'), max_length=50, choices=CHARITY_TYPE_CHOICES, blank=True)
    email = models.EmailField(_('LM Contact Email'), blank=True)
    telephone = models.CharField(_('Tel Number'), max_length=30, blank=True)
    website = models.URLField(_('Website'), blank=True)
    reserves = models.CharField(_('LM Reserves'), max_length=50, blank=True)
    deficit = models.CharField(_('LM Surplus/Deficit'), max_length=50, blank=True)
    statement = models.TextField(_('Mission Statement'), blank=True)
    hours = models.TextField(_('Opening Hours'), blank=True)
    group_avatar = models.ImageField(_('LM Profile Image'), upload_to='localminds/avatars/', blank=True)

    # Data, entered in Step 3.
    ceo_one = models.ForeignKey('Person', related_name='ceo_one_of', null=True, blank=True)
    ceo_two = models.ForeignKey('Person', related_name='ceo_two_of', null=True, blank=True)
    chair = models.ForeignKey('Person', related_name='chair_one_of', null=True, blank=True)

    staff_count = models.PositiveIntegerField(_('No Of Staff'), null=True, blank=True)
    trustees_count = models.PositiveIntegerField(_('No Of Trustees'), null=True, blank=True)
    volunteers_count = models.PositiveIntegerField(_('No Of Volunteers'), null=True, blank=True)
    trustees_active = models.PositiveIntegerField(_('No Of Trustees Who Use MH Services'), null=True, blank=True)
    area_of_benefit = models.CharField(_('Area of benefit'), max_length=50, blank=True)
    average_volunteer_hours = models.CharField(_('Average volunteer hours'), max_length=50, blank=True)

    created = CreationDateTimeField()
    modified = ModificationDateTimeField()

    class Meta:
        verbose_name = _('Local Mind')
        verbose_name_plural = _('Local Minds')

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return 'local-mind', (), {'slug': self.slug}


class Ethnicity(models.Model):
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = _('Ethnicity')
        verbose_name_plural = _('Ethnicities')

    def __unicode__(self):
        return self.name


class Person(models.Model):
    GENDER_CHOICES = (
        ('female', _('Female')),
        ('male', _('Male')),
    )

    name = models.CharField(max_length=50)
    ethnicity = models.ForeignKey('Ethnicity', null=True, blank=True)
    gender = models.CharField(max_length=30, choices=GENDER_CHOICES, blank=True)
    email = models.EmailField(blank=True)
    telephone = models.CharField(max_length=30, blank=True)
