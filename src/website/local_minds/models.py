from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.fields import AutoSlugField, CreationDateTimeField, ModificationDateTimeField


class LocalMind(models.Model):
    CHARITY_TYPE_CHOICES = (
        ('unincorporated', _('Unincorporated'),),
        ('company-limited-by-guarantee', _('Company Limited by Guarantee'),),
        ('charitable-incorporated-organisation', _('Charitable Incorporated Organisation'),),
    )

    name = models.CharField(_('Local Mind'), max_length=120)
    slug = AutoSlugField(populate_from=('name',))

    region = models.CharField(_('Region'), max_length=50, blank=True)
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
    group_avatar = models.ImageField(_('LM Profile Image'), upload_to='localminds/avatars/', blank=True)

    # Data, entered in Step 3.
    # remove 'chairman, chairman_email, ceo, ceo_email, ceo_telephone, chair ethnicity'
    chairman = models.CharField(_('Chairs name'), max_length=50, blank=True)
    chairman_email = models.EmailField(_('Email'), blank=True)
    ceo = models.CharField(_('CEO Name'), max_length=50, blank=True)
    ceo_email = models.EmailField(_('CEO Email'), blank=True)
    ceo_telephone = models.CharField(_('CEO Contact'), max_length=30, blank=True)
    chair_ethnicity = models.ForeignKey('Ethnicity', verbose_name=_('Chair Ethnicity'), related_name='chair_ethnicity+', null=True, blank=True)
    # adding
    # ceo_one = models.CharField(_('CEO One Name'), max_length=50, blank=True)
    # ceo_one_ethnicity = models.ForeignKey('Ethnicity', verbose_name=_('Chair Ethnicity'), related_name='chair_ethnicity+', null=True, blank=True)
    # ceo_one_gender = model COICES
    # ceo_one_email = models.EmailField(_('CEO Email'), blank=True)
    # ceo_one_telephone = models.CharField(_('CEO Contact'), max_length=30, blank=True)
    # ceo_two = models.CharField(_('CEO One Name'), max_length=50, blank=True)
    # ceo_two_ethnicity = models.ForeignKey('Ethnicity', verbose_name=_('Chair Ethnicity'), related_name='chair_ethnicity+', null=True, blank=True)
    # ceo_two_gender = model COICES
    # ceo_two_email = models.EmailField(_('CEO Email'), blank=True)
    # ceo_two_telephone = models.CharField(_('CEO Contact'), max_length=30, blank=True)
    # chair = models.CharField(_('CEO One Name'), max_length=50, blank=True)
    # chair_ethnicity = models.ForeignKey('Ethnicity', verbose_name=_('Chair Ethnicity'), related_name='chair_ethnicity+', null=True, blank=True)
    # chair_gender = model COICES
    # chair_email = models.EmailField(_('CEO Email'), blank=True)
    # chair_telephone = models.CharField(_('CEO Contact'), max_length=30, blank=True)
    staff_count = models.PositiveIntegerField(_('No Of Staff'), null=True, blank=True)
    trustees_count = models.PositiveIntegerField(_('No Of Trustees'), null=True, blank=True)
    volunteers_count = models.PositiveIntegerField(_('No Of Volunteers'), null=True, blank=True)
    trustees_active = models.PositiveIntegerField(_('No Of Trustees Who Use MH Services'), null=True, blank=True)
    #remove 'trustees_ethnicities', 'volunteers_ethnicities', 'staff_ethnicities'.
    trustees_ethnicities = models.ManyToManyField('Ethnicity', verbose_name=_('Trustees Ethnicity'), related_name='trustees+', blank=True)
    volunteers_ethnicities = models.ManyToManyField('Ethnicity', verbose_name=_('Volunteers Ethnicity'), related_name='volunteers+', blank=True)
    staff_ethnicities = models.ManyToManyField('Ethnicity', verbose_name=_('Staff Ethnicity'), related_name='staff+', blank=True)
    # adding
    # area_of_benefit = models.CharField(_('max_length=50, blank=True)
    # average_volunteer_hours = models.CharField(_('max_length=50, blank=True)

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
