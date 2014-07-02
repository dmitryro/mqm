from django.db import models
from tinymce.widgets import TinyMCE


def TextEditor():
    return TinyMCE(attrs={'style': 'width: 50%; height: 20em;'})
    
class TinyMCEAdminMixin(object):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE(attrs={'style': 'width:50%; height:20em;'})},
    }
