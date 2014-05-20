from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.fields import AutoSlugField, CreationDateTimeField, ModificationDateTimeField


class LocalMind(models.Model):
    CHARITY_TYPE_CHOICES = (
        ('unincorporated', _('Unincorporated'),),
        ('company-limited-by-guarantee', _('Company Limited by Guarantee'),),
        ('charitable-incorporated-organisation', _('Charitable Incorporated Organisation'),),
    )

    ETHNICITY_CHOICES = (
        ('british', _('British')),
    )

    name = models.CharField(_('Local Mind'), max_length=120)
    slug = AutoSlugField(populate_from=('name',))

    region = models.CharField(_('Region'), max_length=50)
    address = models.TextField(_('Address'))
    postcode = models.CharField(_('Postcode'), max_length=50)
    income_restricted = models.CharField(_('LM Income R'), max_length=50)
    income_unrestricted = models.CharField(_('LM Income U'), max_length=50)
    charity_no = models.CharField(_('Charity Number'), max_length=30)
    charity_type = models.CharField(_('Charity Type'), max_length=50, choices=CHARITY_TYPE_CHOICES)
    email = models.EmailField(_('LM Contact Email'))
    telephone = models.CharField(_('Tel Number'), max_length=30)
    website = models.URLField(_('Website'))
    reserves = models.CharField(_('LM Reserves'), max_length=50)
    deficit = models.CharField(_('LM Surplus/Deficit'), max_length=50)
    statement = models.TextField(_('Mission Statement'))
    group_avatar = models.ImageField(_('LM Profile Image'), upload_to='localminds/avatars/')

    # Data, entered in Step 3.

    chairman = models.CharField(_('Chairs name'), max_length=50)
    chairman_email = models.EmailField(_('Email'))
    ceo = models.CharField(_('CEO Name'), max_length=50)
    ceo_email = models.EmailField(_('CEO Email'))
    ceo_telephone = models.CharField(_('CEO Contact'), max_length=30)
    chair_ethnicity = models.CharField(_('Chair Ethnicity'), max_length=50, choices=ETHNICITY_CHOICES)
    staff_count = models.PositiveIntegerField(_('No Of Staff'), null=True)
    trustees_count = models.PositiveIntegerField(_('No Of Trustees'))
    volunteers_count = models.PositiveIntegerField(_('No Of Volunteers'))
    trustees_active = models.PositiveIntegerField(_('No Of Trustees Who Use MH Services'))
    trustees_ethnicity = models.CharField(_('Trustees Ethnicity'), max_length=50, choices=ETHNICITY_CHOICES)
    volunteers_ethnicity = models.CharField(_('Volunteers Ethnicity'), max_length=50, choices=ETHNICITY_CHOICES)
    staff_ethnicity = models.CharField(_('Staff Ethnicity'), max_length=50, choices=ETHNICITY_CHOICES)

    created = CreationDateTimeField()
    modified = ModificationDateTimeField()

    class Meta:
        verbose_name = _('Local Mind')
        verbose_name_plural = _('Local Minds')

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return 'localmind', (), {'slug': self.slug}
