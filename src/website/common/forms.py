from floppyforms.__future__.models import ModelForm


class NodeForm(ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(NodeForm, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.instance.user = self.user
        self.instance.local_mind = self.user.local_mind
        return super(NodeForm, self).save(*args, **kwargs)
