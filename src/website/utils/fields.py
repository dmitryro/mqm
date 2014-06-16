from django.db import models
import floppyforms as forms


class EmailField(models.EmailField):
    def get_prep_value(self, value):
        value = super(EmailField, self).get_prep_value(value)
        if value is not None:
            value = value.lower()
        return value

    def formfield(self, **kwargs):
        kwargs.setdefault('form_class', forms.EmailField)
        return super(EmailField, self).formfield(**kwargs)


from south.modelsinspector import add_introspection_rules
add_introspection_rules([], ["^website\.utils\.fields\.EmailField"])
