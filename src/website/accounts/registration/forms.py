from datetime import datetime
from django.forms.formsets import formset_factory
from django.forms.models import inlineformset_factory
from django.utils.translation import ugettext_lazy as _
from django_compositeform import CompositeModelForm, ForeignKeyFormField, FormSetField, InlineFormSetField

import website.floppyforms_patch
from floppyforms.__future__.models import ModelForm, formfield_callback
import floppyforms.__future__ as forms

from website.accounts.models import User, Experience
from website.faq.models import Question
from website.local_map.models import Map
from website.local_minds.models import LocalMind, Ethnicity, Person
from website.news.models import PositiveNews
from website.resources.models import Resource
from website.services.models import Service
from website.tasks.models import Task


class SignupLocalMindForm(ModelForm):
    accept_tos = forms.BooleanField(label=_('Terms'), required=True,
        help_text=_(
            'We (above LM) agree to all terms and conditions of the openhub '
            'site.'))

    class Meta:
        model = LocalMind
        fields = (
            'name',
            'region',
            'address',
            'postcode',
            'income_restricted',
            'charity_no',
            'charity_type',
            'email',
            'telephone',
            'website',
            'income_unrestricted',
            'reserves',
            'deficit',
            'statement',
            'hours',
            'group_avatar',
        )

    def save(self, *args, **kwargs):
        reserved_email = kwargs.pop('reserved_email')
        if reserved_email.local_mind:
            self.instance.reserved_local_mind = reserved_email.local_mind
        return super(SignupLocalMindForm, self).save(*args, **kwargs)


class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = ('experience',)


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ('text',)


class InlineTaskFormSetField(InlineFormSetField):
    def get_formset_class(self, form, name):
        '''
        Set ``local_mind`` and ``created_by`` on task instances.
        '''
        user = form.instance

        FormSetClass = super(InlineTaskFormSetField, self).\
            get_formset_class(form, name)

        class NewFormSetClass(FormSetClass):
            def save_new(self, form, commit=True):
                form.instance.local_mind = user.local_mind
                form.instance.created_by = user
                return super(NewFormSetClass, self).save_new(form, commit=commit)

        return NewFormSetClass


class BaseSignupProfileForm(CompositeModelForm):
    formfield_callback = formfield_callback

    user_privileges = None

    error_messages = {
        'password_mismatch': _("The two password fields didn't match."),
    }

    password1 = forms.CharField(label=_('Password'), widget=forms.PasswordInput)
    password2 = forms.CharField(label=_('Re-enter password'), widget=forms.PasswordInput)

    experiences = InlineFormSetField(
        parent_model=User,
        model=Experience,
        form=ExperienceForm,
        can_delete=False,
        extra=4,
        max_num=4)
    tasks = InlineTaskFormSetField(
        parent_model=User,
        model=Task,
        form=TaskForm,
        fk_name='assigned_to',
        can_delete=False)

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'job_title',
            'skills',
            'user_avatar',
            'biography',
            'telephone',
            'twitter',
        )

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'])
        return password2

    def clean_twitter(self):
        value = self.cleaned_data['twitter']
        if value:
            value = value.lstrip('@')
        return value

    def save(self, *args, **kwargs):
        self.instance.set_password(self.cleaned_data["password1"])
        self.instance.privileges = self.user_privileges
        return super(BaseSignupProfileForm, self).save(*args, **kwargs)


class SignupProfileForm(BaseSignupProfileForm):
    formfield_callback = formfield_callback

    user_privileges = User.SUPERUSER

    def save(self, email, local_mind, *args, **kwargs):
        self.instance.email = email
        self.instance.local_mind = local_mind
        return super(SignupProfileForm, self).save(*args, **kwargs)


class SignupUserProfileForm(BaseSignupProfileForm):
    '''
    This profile form is used for single persons that only get to see this
    form, not the whole signup process.
    '''

    formfield_callback = formfield_callback

    user_privileges = User.TRUSTEE

    def save(self, *args, **kwargs):
        self.instance.date_joined = datetime.utcnow()
        return super(SignupUserProfileForm, self).save(*args, **kwargs)


class SelectEthnicityForm(forms.Form):
    ethnicity = forms.ModelChoiceField(
        label=_('Ethnicity'),
        queryset=Ethnicity.objects.all())


EthnicityFormSet = formset_factory(
    form=SelectEthnicityForm,
    extra=1)


class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = (
            'name',
            'type',
            'users_count',
        )


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = (
            'question',
            'notifications',
            'privacy',
        )


class PersonForm(ModelForm):
    class Meta:
        model = Person
        significant_fields = ('name',)
        fields = (
            'name',
            'ethnicity',
            'gender',
            'email',
            'telephone',
        )


class SignupLocalMindMembersForm(CompositeModelForm):
    formfield_callback = formfield_callback

    ceo_one = ForeignKeyFormField(PersonForm)
    ceo_two = ForeignKeyFormField(PersonForm)
    chair = ForeignKeyFormField(PersonForm)

#    services = InlineFormSetField(
#        parent_model=LocalMind,
#        model=Service,
#        form=ServiceForm,
#        extra=3,
#        can_delete=False)
    faqs = InlineFormSetField(
        parent_model=LocalMind,
        model=Question,
        form=QuestionForm,
        extra=3,
        can_delete=False)

    class Meta:
        model = LocalMind
        fields = (
            'staff_count',
            'trustees_count',
            'volunteers_count',
            'trustees_active',
            'area_of_benefit',
            'average_volunteer_hours',
        )

    def get_objects_from_formset(self, name):
        formset = self.formsets[name]
        return [
            form.cleaned_data['ethnicity']
            for form in formset.forms
            if form.is_valid() and 'ethnicity' in form.cleaned_data]

    def save(self, local_mind, *args, **kwargs):
        # Hijack instance with new version.
        self.instance = local_mind
#        self.formsets['services'].instance = local_mind
        self.formsets['faqs'].instance = local_mind

        instance = super(SignupLocalMindMembersForm, self).save(*args, **kwargs)
        return instance


class ResourceForm(ModelForm):
    class Meta:
        model = Resource
        fields = (
            'name',
            'privacy',
        )


class MapForm(ModelForm):
    class Meta:
        model = Map
        fields = (
            'name',
            'email',
            'address',
            'telephone',
            'relationship',
            'postcode',
            'category',
            'website',
            'privacy',
        )


class PositiveNewsForm(ModelForm):
    class Meta:
        model = PositiveNews
        fields = (
            'title',
            'description',
            'date',
            'tags',
        )
        widgets = {
            'tags': forms.TextInput,
        }


class SignupPartnersForm(CompositeModelForm):
    formfield_callback = formfield_callback

    resources = InlineFormSetField(
        parent_model=LocalMind,
        model=Resource,
        form=ResourceForm,
        extra=3,
        can_delete=False)
    key_partners = InlineFormSetField(
        parent_model=LocalMind,
        model=Map,
        form=MapForm,
        extra=1,
        can_delete=False)
    positive_news = InlineFormSetField(
        parent_model=LocalMind,
        model=PositiveNews,
        form=PositiveNewsForm,
        extra=1,
        can_delete=False)

    class Meta:
        model = LocalMind
        fields = ()

    def save(self, local_mind, user, *args, **kwargs):
        # Hijack instance with new version.
        self.instance = local_mind
        for formset in self.formsets.values():
            formset.instance = local_mind

        for form in self.formsets['positive_news'].forms:
            form.instance.author = user

        for form in self.formsets['key_partners'].forms:
            form.instance.user = user

        return super(SignupPartnersForm, self).save(*args, **kwargs)


class InvitationForm(ModelForm):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'privileges',
            'job_title',
        )

    def save(self, *args, **kwargs):
        self.instance.local_mind = self.cleaned_data['local_mind']
        self.instance.date_joined = None
        saved_obj = super(InvitationForm, self).save(*args, **kwargs)
        def send_invitation():
            saved_obj.send_invitation()
        self.save_m2m = send_invitation
        return saved_obj


class SignupInviteForm(CompositeModelForm):
    invites = InlineFormSetField(
        parent_model=LocalMind,
        model=User,
        form=InvitationForm,
        extra=3,
        can_delete=False)

    class Meta:
        model = LocalMind
        fields = ()

    def save(self, local_mind, *args, **kwargs):
        # Hijack instance with new version.
        self.instance = local_mind
        for formset in self.formsets.values():
            formset.instance = local_mind
            for form in formset.forms:
                if form.has_changed():
                    form.cleaned_data['local_mind'] = local_mind
        return super(SignupInviteForm, self).save(*args, **kwargs)
