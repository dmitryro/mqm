from django.forms.formsets import formset_factory
from django.forms.models import inlineformset_factory
from django.utils.translation import ugettext_lazy as _
from django_compositeform import CompositeModelForm, ForeignKeyFormField, FormSetField, InlineFormSetField
import floppyforms as forms

from website.accounts.models import User, Experience
from website.faq.models import Question
from website.local_map.models import Map
from website.local_minds.models import LocalMind, Ethnicity, Person
from website.news.models import PositiveNews
from website.resources.models import Resource
from website.services.models import Service
from website.tasks.models import Task


class SignupLocalMindForm(forms.ModelForm):
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


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ('experience',)


class TaskForm(forms.ModelForm):
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


class SignupProfileForm(CompositeModelForm):
    error_messages = {
        'password_mismatch': _("The two password fields didn't match."),
    }

    password1 = forms.CharField(label=_('Password'), widget=forms.PasswordInput)
    password2 = forms.CharField(label=_('Re-enter password'), widget=forms.PasswordInput)

    experiences = InlineFormSetField(
        parent_model=User,
        model=Experience,
        form=ExperienceForm,
        can_delete=False)
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
            'mobile',
            'twitter',
        )

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'])
        return password2

    def save(self, reserved_email, local_mind, *args, **kwargs):
        self.instance.email = reserved_email.email
        self.instance.local_mind = local_mind
        self.instance.set_password(self.cleaned_data["password1"])
        self.instance.privileges = 'superuser'
        return super(SignupProfileForm, self).save(*args, **kwargs)


class SelectEthnicityForm(forms.Form):
    ethnicity = forms.ModelChoiceField(
        label=_('Ethnicity'),
        queryset=Ethnicity.objects.all())


EthnicityFormSet = formset_factory(
    form=SelectEthnicityForm,
    extra=1)


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = (
            'name',
            'type',
            'users_count',
        )


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = (
            'question',
            'notifications',
            'privacy',
        )


class PersonForm(forms.ModelForm):
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
    ceo_one = ForeignKeyFormField(PersonForm, kwargs={'empty_permitted': True})
    ceo_two = ForeignKeyFormField(PersonForm, kwargs={'empty_permitted': True})
    chair = ForeignKeyFormField(PersonForm, kwargs={'empty_permitted': True})

    services = InlineFormSetField(
        parent_model=LocalMind,
        model=Service,
        form=ServiceForm,
        extra=3,
        can_delete=False)
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
        self.formsets['services'].instance = local_mind
        self.formsets['faqs'].instance = local_mind

        instance = super(SignupLocalMindMembersForm, self).save(*args, **kwargs)
        return instance


class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = (
            'name',
            'privacy',
        )


class MapForm(forms.ModelForm):
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


class PositiveNewsForm(forms.ModelForm):
    class Meta:
        model = PositiveNews
        fields = (
            'title',
            'description',
            'date',
            'tags',
        )


class SignupPartnersForm(CompositeModelForm):
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

        return super(SignupPartnersForm, self).save(*args, **kwargs)


class InvitationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'privileges',
            'job_title',
        )


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
        return super(SignupInviteForm, self).save(*args, **kwargs)
