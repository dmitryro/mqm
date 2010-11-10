from django.db import models
from tinymce.widgets import TinyMCE


class TinyMCEAdminMixin(object):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE(attrs={'style': 'width:50%; height:20em;'})},
    }
